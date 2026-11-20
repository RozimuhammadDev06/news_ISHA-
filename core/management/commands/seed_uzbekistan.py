from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from PIL import Image

from core.models import Category, New


class Command(BaseCommand):
    help = 'Add 12 sample articles with existing project images to category 8.'

    def handle(self, *args, **options):
        category = Category.objects.get(pk=8, slug='ozbekiston')
        images = []
        for path in sorted((Path(settings.MEDIA_ROOT) / 'news').iterdir()):
            if path.is_file():
                try:
                    with Image.open(path) as image:
                        image.verify()
                    images.append(path.relative_to(settings.MEDIA_ROOT).as_posix())
                except (OSError, ValueError):
                    continue
        if len(images) < 12:
            raise CommandError('At least 12 valid local images are required.')
        topics = [
            'O‘zbekiston bo‘ylab sayohat', 'Toshkentning zamonaviy qiyofasi',
            'Samarqandning tarixiy obidalari', 'Buxoroning madaniy merosi',
            'Xivaning qadimiy ko‘chalari', 'O‘zbekistonda ta’lim imkoniyatlari',
            'Yoshlar va sport', 'Milliy hunarmandchilik an’analari',
            'Tabiat va atrof-muhit', 'O‘zbekistonning transport yo‘llari',
            'Mahallalarda kundalik hayot', 'O‘zbek milliy madaniyati',
        ]
        created_count = 0
        with transaction.atomic():
            for number, (topic, image) in enumerate(zip(topics, images), 1):
                description = f'Namuna material: {topic}. Bu yozuv sayt ko‘rinishini sinash uchun qo‘shilgan; rasm loyiha kutubxonasidan olingan.'
                _, created = New.objects.get_or_create(
                    tags=f'uzbekistan-sample-{number:02d}',
                    defaults=dict(category=category, title=f'{topic} (namuna)',
                                  short_desc=description, description=description,
                                  image=image, views=0),
                )
                created_count += created
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} sample articles in category {category.pk}.'))
