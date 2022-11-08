from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from .models import Category, Item, Tag


class StaticURLTests(TestCase):
    def test_catalog_main_page_endpoint(self):
        response = Client().get('/catalog')
        self.assertEqual(response.status_code, 301)

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
                'primary_key': 0,
                'necessary_status': 404,
                'description': 'Testing zero'
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


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=150
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    # Testing Item model
    def test_unable_create_item(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            item = Item(
                name='Test item',
                category=self.category,
                text='Test description'
            )

            item.full_clean()
            item.save()
            item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_item(self):
        tests = (
            (
                Item(
                    name='Test item',
                    category=self.category,
                    text='Test description роскошно'
                ),
                'Testing with "роскошно"'
            ),
            (
                Item(
                    name='Test item',
                    category=self.category,
                    text='Test description превосходно'
                ),
                'Testing with "превосходно"'
            )
        )

        for test in tests:
            with self.subTest(test[1]):
                item_count = Item.objects.count()

                item = test[0]
                item.full_clean()
                item.save()
                item.tags.add(self.tag)

                self.assertEqual(Item.objects.count(), item_count + 1)

    # Testing Category model
    def test_unable_create_category(self):
        categories_count = Category.objects.count()

        tests = [
            (0, 'Testing zero'),
            (-1, 'Testing negative'),
            (32767, 'Testing 32767'),
            (100000, 'Testing big int')
        ]

        for test in tests:
            with self.subTest(test[1]):
                with self.assertRaises(ValidationError):
                    category = Category(
                        weight=test[0],
                        name='Test category',
                        is_published=True,
                        slug=f'test-category-slug-{test[0]}'
                    )

                    category.full_clean()
                    category.save()

        self.assertEqual(Category.objects.count(), categories_count)

    def test_able_to_create_category(self):
        categories_count = Category.objects.count()

        category = Category(
            weight=1111,
            name='Test category',
            is_published=True,
            slug='test-category-slug-777'
        )
        category.full_clean()
        category.save()

        self.assertEqual(Category.objects.count(), categories_count + 1)
