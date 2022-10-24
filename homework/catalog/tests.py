from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_catalog_main_page_without_slash_endpoint(self):
        response = Client().get('/catalog')
        self.assertEqual(response.status_code, 301)

    def test_catalog_main_page_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_numeric_item_endpoint(self):
        response = Client().get('/catalog/777/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_negative_numeric_item_endpoint(self):
        response = Client().get('/catalog/-20/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_zero_item_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_not_numeric_item_endpoint(self):
        response = Client().get('/catalog/azino/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_mixed_item_endpoint(self):
        response = Client().get('/catalog/azino777/')
        self.assertEqual(response.status_code, 404)
