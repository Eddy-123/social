from django.urls import resolve
from django.test import TestCase
from social.settings import DEFAULT_AUTO_FIELD
from .views import post_list


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, post_list)
