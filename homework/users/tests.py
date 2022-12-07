from django.test import Client, TestCase
from datetime import date, timedelta
from .models import User as Profile
from django.urls import reverse


class ModelsTest(TestCase):
    def test_birthday_correct_context_empty_users(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn(
            "birthday_today",
            response.context,
        )

    def test_birthday_correct_context(self):
        Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=5)
        )
        Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get(reverse('homepage:home'))
        self.assertIn(
            "birthday_today",
            response.context,
        )

    def test_birthday_show_correct_context_null(self):
        Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=5)
        )
        Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(len(response.context["birthday_today"]), 0)

    def test_birthday_show_correct_context_not_null(self):
        Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday=date.today()
        )
        Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get(reverse('catalog:home'))
        self.assertEqual(len(response.context["birthday_today"]), 1)

    def test_birthday_show_correct_context(self):
        Profile.objects.create_user(
            first_name="test1", email="test3@gmail.com", password="1234abcd",
            birthday=date.today()
        )
        Profile.objects.create_user(
            first_name="test2", email="test4@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(len(response.context["birthday_today"]), 1)
        self.assertEqual(
            response.context["birthday_today"][0].email, "test3@gmail.com")
