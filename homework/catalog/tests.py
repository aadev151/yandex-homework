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
        tests = (
            {
                'primary_key': 123,
                'necessary_status': 200,
                'description': 'Testing positive int'
            },
            {
                'primary_key': 15.73,
                'necessary_status': 404,
                'description': 'Testing float'
            },
            {
                'primary_key': -15,
                'necessary_status': 404,
                'description': 'Testing negative int'
            },
            {
                'primary_key': 'azino',
                'necessary_status': 404,
                'description': 'Testing string'
            },
            {
                'primary_key': '1234567u',
                'necessary_status': 404,
                'description': 'Testing mixed string'
            }
        )

        for test in tests:
            with self.subTest(test['description']):
                response = Client().get(
                    f'/catalog/{test["primary_key"]}/'
                )
                self.assertEqual(
                    response.status_code,
                    test['necessary_status']
                )
