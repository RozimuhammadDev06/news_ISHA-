from django.test import TestCase
from django.urls import reverse
from .models import Category, New
from .models import User
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    def registration_data(self, **overrides):
        data = {
            'name': 'Aziz', 'surname': 'Karimov', 'age': 23,
            'phone_number': '+998 (90) 123-45-67', 'second_number': '',
            'email': 'aziz@example.com', 'location': 'Toshkent',
            'password': 'River!Cloud2026', 'password_conf': 'River!Cloud2026',
        }
        data.update(overrides)
        return data

    def test_account_pages_and_navigation(self):
        for page in ('login', 'register'):
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'csrfmiddlewaretoken')
            self.assertContains(response, 'css/auth.css')
        self.assertContains(self.client.get(reverse('home')), 'href="/login/"')

    def test_register_hashes_password_and_logs_in(self):
        response = self.client.post(reverse('register'), self.registration_data(role='admin'))
        self.assertRedirects(response, reverse('home'))
        user = User.objects.get()
        self.assertEqual(user.phone_number, '+998901234567')
        self.assertTrue(user.check_password('River!Cloud2026'))
        self.assertNotEqual(user.password, 'River!Cloud2026')
        self.assertEqual(user.password_conf, '')
        self.assertEqual(user.role, 'user')
        self.assertIsNotNone(user.last_login)
        self.assertEqual(self.client.session['_auth_user_id'], str(user.pk))
        self.assertContains(self.client.get(reverse('home')), 'Aziz')
        self.assertRedirects(self.client.get(reverse('login')), reverse('home'))
        self.assertRedirects(self.client.get(reverse('register')), reverse('home'))

    def test_invalid_registration_does_not_create_user(self):
        for changes in (
            {'password_conf': 'different'}, {'password': '123', 'password_conf': '123'},
            {'age': -1}, {'phone_number': 'abc901234567'}, {'email': 'invalid'},
            {'name': ''},
        ):
            with self.subTest(changes=changes):
                response = self.client.post(reverse('register'), self.registration_data(**changes))
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.context['form'].errors)
                self.assertFalse(User.objects.exists())

    def test_duplicate_normalized_phone(self):
        self.client.post(reverse('register'), self.registration_data())
        self.client.post(reverse('logout'))
        response = self.client.post(reverse('register'), self.registration_data(phone_number='901234567'))
        self.assertContains(response, 'hisob allaqachon ochilgan')
        self.assertEqual(User.objects.count(), 1)

    def test_login_logout_and_invalid_credentials(self):
        self.client.post(reverse('register'), self.registration_data())
        self.client.post(reverse('logout'))
        for phone, password in [('901234567', 'wrong'), ('909999999', 'River!Cloud2026')]:
            response = self.client.post(reverse('login'), {'phone_number': phone, 'password': password})
            self.assertContains(response, 'Telefon raqami yoki parol noto‘g‘ri.')
            self.assertNotIn('_auth_user_id', self.client.session)
        response = self.client.post(reverse('login'), {'phone_number': '90 123 45 67', 'password': 'River!Cloud2026'})
        self.assertRedirects(response, reverse('home'))
        self.assertContains(self.client.get(reverse('home')), 'Aziz')
        self.assertEqual(self.client.get(reverse('logout')).status_code, 405)
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(self.client.post(reverse('logout')), reverse('home'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_password_change_invalidates_existing_session(self):
        self.client.post(reverse('register'), self.registration_data())
        user = User.objects.get()
        user.set_password('Different!Secret2026')
        user.save()
        self.assertContains(self.client.get(reverse('home')), 'href="/login/"')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_csrf_is_required(self):
        from django.test import Client

        client = Client(enforce_csrf_checks=True)
        for page in ('login', 'register', 'logout'):
            self.assertEqual(client.post(reverse(page), {}).status_code, 403)

    def test_admin_login_still_works(self):
        admin = get_user_model().objects.create_superuser('siteadmin', 'admin@example.com', 'Strong!Pass2026')
        response = self.client.post(reverse('admin:login'), {
            'username': admin.username, 'password': 'Strong!Pass2026', 'next': reverse('admin:index'),
        })
        self.assertRedirects(response, reverse('admin:index'))

class CategoryPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Avoid external category notifications during isolated tests.
        Category.objects.bulk_create([
            Category(cat_name='Sport', slug='sport'),
            Category(cat_name='Iqtisod', slug='iqtisod'),
            Category(cat_name='Empty', slug='empty'),
        ])
        sport = Category.objects.get(slug='sport')
        economy = Category.objects.get(slug='iqtisod')
        New.objects.bulk_create([
            New(title=f'Sport article {n}', short_desc='Summary', description='Content',
                tags=f'sport-{n}', category=sport, image='news/test.jpg') for n in range(7)
        ] + [New(title='Economy only article', short_desc='Summary', description='Content',
                 tags='economy', category=economy, image='news/test.jpg')])

    def test_filtering_and_pagination(self):
        url = reverse('ctg', args=['sport'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 6)
        self.assertEqual(response.context['page_obj'].paginator.count, 7)
        self.assertTrue(all(i.category.slug == 'sport' for i in response.context['popular_news']))
        self.assertNotContains(response, 'Economy only article')
        self.assertEqual(len(self.client.get(url, {'page': 2}).context['page_obj']), 1)

    def test_empty_and_unknown_categories(self):
        self.assertContains(self.client.get(reverse('ctg', args=['empty'])), 'Bu kategoriyada hozircha')
        self.assertEqual(self.client.get(reverse('ctg', args=['missing'])).status_code, 404)

    def test_home_menu(self):
        self.assertContains(self.client.get(reverse('home')), 'href="/ctg/sport/"')
