from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_catalog_main_page_endpoint(self):
        # Testing the main page without slash
        response = Client().get('/catalog')
        self.assertEqual(response.status_code, 301)

        # Testing the main page
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_items_endpoint(self):
        # Testing numeric items
        for pk in range(1, 10000):
            with self.subTest(f'Testing /catalog/{pk}'):
                response = Client().get(f'/catalog/{pk}/')
                self.assertEqual(response.status_code, 200)

        # Testing a negative numeric item
        response = Client().get('/catalog/-20/')
        self.assertEqual(response.status_code, 404)

        # Testing item 0
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

        # Testing float items
        primary_keys = [.05 * i for i in range(1, 41)]
        for pk in primary_keys:
            with self.subTest(f'Testing /catalog/{pk}'):
                response = Client().get(f'/catalog/{pk}/')
                self.assertEqual(response.status_code, 404)

        # Testing a not numeric item
        response = Client().get('/catalog/azino/')
        self.assertEqual(response.status_code, 404)

        # Testing a mixed item
        response = Client().get('/catalog/azino777/')
        self.assertEqual(response.status_code, 404)
