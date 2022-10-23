from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_about_page_without_slash_endpoint(self):
        response = Client().get('/about')
        self.assertEqual(response.status_code, 301)

    def test_about_page_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)
