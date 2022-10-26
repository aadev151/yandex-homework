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

        tests = tuple(
            # Testing int items
            [
                {
                    'primary_key': pk,
                    'necessary_status': 200,
                    'description': f'Testing /catalog/{pk}/'
                }
                for pk in range(1, 200)
            ] +

            # Testing float items
            [
                {
                    'primary_key': pk,
                    'necessary_status': 404,
                    'description': f'Testing /catalog/{pk}/'
                }
                for pk in [.05 * i for i in range(1, 41)]
            ] +

            # Testing zero and negative int items
            [
                {
                    'primary_key': pk,
                    'necessary_status': 404,
                    'description': f'Testing /catalog/{pk}/'
                }
                for pk in range(-20, 1)
            ] +

            # Testing strings and mixed items
            [
                {
                    'primary_key': 'azino',
                    'necessary_status': 404,
                    'description': 'Testing /catalog/azino/'
                },
                {
                    'primary_key': 'hey123',
                    'necessary_status': 404,
                    'description': 'Testing /catalog/hey123/'
                },
                {
                    'primary_key': 'p12i',
                    'necessary_status': 404,
                    'description': 'Testing /catalog/p12i/'
                },
                {
                    'primary_key': '1234567u',
                    'necessary_status': 404,
                    'description': 'Testing /catalog/1234567u/'
                }
            ]
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
