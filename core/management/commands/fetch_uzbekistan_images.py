import json
from io import BytesIO
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from PIL import Image
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from django.db import transaction

from core.models import New


class Command(BaseCommand):
    help = 'Download topic-matched Wikipedia images for the 12 sample articles.'

    def handle(self, *args, **options):
        topics = [
            'Tourism in Uzbekistan', 'Tashkent', 'Registan', 'Po-i-Kalyan',
            'Itchan Kala', 'National University of Uzbekistan', 'Pakhtakor Central Stadium',
            'Suzani (textile)', 'Chimgan', 'Tashkent–Bukhara high-speed rail line', 'Chorsu Bazaar',
            'Uzbek cuisine',
        ]
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=Retry(
            total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504],
        )))
        session.headers['User-Agent'] = 'UzbekistanNewsDemo/1.0 (educational local website)'
        records = []
        staged = []
        result = session.get('https://en.wikipedia.org/w/api.php', params={
            'action': 'query', 'format': 'json', 'prop': 'pageimages',
            'piprop': 'thumbnail|name', 'pithumbsize': 1000, 'pilicense': 'free',
            'titles': '|'.join(topics), 'redirects': 1,
        }, timeout=30)
        result.raise_for_status()
        pages = {page['title']: page for page in result.json()['query']['pages'].values()}
        metadata = session.get('https://en.wikipedia.org/w/api.php', params={
            'action': 'query', 'format': 'json', 'prop': 'imageinfo',
            'iiprop': 'url|extmetadata',
            'titles': '|'.join('File:' + page['pageimage'] for page in pages.values() if 'pageimage' in page),
        }, timeout=30)
        metadata.raise_for_status()
        for number, topic in enumerate(topics, 1):
            article = New.objects.get(tags=f'uzbekistan-sample-{number:02d}', category_id=8)
            page = pages.get(topic, {})
            if 'thumbnail' not in page:
                raise CommandError(f'No free image found for {topic}')
            url = page['thumbnail']['source']
            storage = article.image.storage
            filename = f'news/uzbekistan-topic-{number:02d}.jpg'
            if storage.exists(filename):
                saved = filename
            else:
                response = session.get(url, timeout=45)
                response.raise_for_status()
                with Image.open(BytesIO(response.content)) as photo:
                    photo.verify()
                extension = '.png' if 'png' in response.headers.get('Content-Type', '') else '.jpg'
                saved = storage.save(f'news/uzbekistan-topic-{number:02d}{extension}', ContentFile(response.content))
            staged.append((article, saved))
            records.append(dict(tag=article.tags, title=article.title, topic=topic,
                                source_page=f'https://en.wikipedia.org/wiki/{topic.replace(" ", "_")}',
                                image_url=url, local_image=saved, attribution=metadata.json()))
            self.stdout.write(f'{number}/12 downloaded: {topic}')
        with transaction.atomic():
            for article, saved in staged:
                article.image = saved
                article.short_desc = f'Namuna material: {article.title.removesuffix(" (namuna)")}. Bu yozuv sayt ko‘rinishini sinash uchun qo‘shilgan.'
                article.description = article.short_desc
                article.save(update_fields=['image', 'short_desc', 'description'])
        destination = Path(settings.MEDIA_ROOT) / 'uzbekistan-image-sources.json'
        destination.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
        self.stdout.write(self.style.SUCCESS('Updated 12 article images; source credits saved.'))
