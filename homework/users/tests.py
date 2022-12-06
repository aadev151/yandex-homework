from django.test import Client, TestCase
from datetime import date, timedelta
from .models import User as Profile


class ModelsTest(TestCase):
    def test_birthday_show_correct_context(self):
        self.user = Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=5)
        )
        self.user2 = Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get("/")
        self.assertIn(
            "birthday_today",
            response.context,
        )
        self.assertEqual(len(response.context["birthday_today"]), 0)

        self.user3 = Profile.objects.create_user(
            first_name="test1", email="test3@gmail.com", password="1234abcd",
            birthday=date.today()
        )
        self.user4 = Profile.objects.create_user(
            first_name="test2", email="test4@gmail.com", password="1234abcd",
            birthday=date.today() - timedelta(days=1)
        )
        response = Client().get("/")
        self.assertEqual(len(response.context["birthday_today"]), 1)
        self.assertEqual(
            response.context["birthday_today"][0].email, "test3@gmail.com")
