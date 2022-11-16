from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Item, Tag


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class PageContextTests(TestCase):

    # Setting up three items that are not visible on the main pge
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=150
        )
        tag = Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

        cls.item1 = Item.objects.create(
            name='Тест 1',
            text='роскошно',
            is_published=True,
            category=category
        )
        cls.item1.tags.add(tag)

        cls.item2 = Item.objects.create(
            name='Тест 2',
            text='роскошно',
            is_published=True,
            category=category,
        )
        cls.item2.tags.add(tag)

        cls.item3 = Item.objects.create(
            name='Тест 3',
            text='роскошно',
            is_published=True,
            category=category
        )
        cls.item3.tags.add(tag)

    def test_homepage_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)

    def test_homepage_context_no_items_on_main_page(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEquals(len(response.context['items']), 0)

    def test_homepage_context_some_items_on_main_page(self):
        self.item1.is_on_main = True
        self.item1.save()
        response = Client().get(reverse('homepage:home'))
        self.assertEquals(len(response.context['items']), 1)
