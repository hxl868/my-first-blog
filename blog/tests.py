from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)  

    def test_post_list_returns_correct_html(self):

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertTemplateUsed(response, 'blog/base.html')

    def test_cv_returns_correct_html(self):
    	response = self.client.get('/cv/')
    	self.assertTemplateUsed(response, 'blog/base.html')
    	self.assertTemplateUsed(response, 'blog/cv.html')