from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from .views import post_list


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/post/list.html")
