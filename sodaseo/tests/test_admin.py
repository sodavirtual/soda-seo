from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from model_mommy import mommy

from sodaseo.models import Config, Template, Url


class TestConfigAdmin(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'user1', 'user1@email.com', '123456'
        )
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='user1', password='123456')

    def test_list(self):
        url = reverse('admin:sodaseo_config_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:sodaseo_config_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_change(self):
        config = mommy.make(Config)
        url = reverse('admin:sodaseo_config_change', args=[config.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestTemplateAdmin(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'user1', 'user1@email.com', '123456'
        )
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='user1', password='123456')

    def test_list(self):
        url = reverse('admin:sodaseo_template_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:sodaseo_template_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_change(self):
        template = mommy.make(Template)
        url = reverse('admin:sodaseo_template_change', args=[template.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestUrlAdmin(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'user1', 'user1@email.com', '123456'
        )
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='user1', password='123456')

    def test_list(self):
        url = reverse('admin:sodaseo_url_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:sodaseo_url_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_change(self):
        url_obj = mommy.make(Url)
        url = reverse('admin:sodaseo_url_change', args=[url_obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
