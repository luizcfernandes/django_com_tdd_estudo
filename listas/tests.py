from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from listas.views import home_page



class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Organizar  (Arrange)
        request = HttpRequest()
        response = home_page(request)

        # Agir (Act)
        html = response.content.decode('utf8')

        # Testar ou afirmar (Assert)
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
