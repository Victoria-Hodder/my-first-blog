from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list

class PostListTest(TestCase):

    def test_root_url_returns_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = post_list(request)  
