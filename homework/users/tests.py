from django.test import Client, TestCase

from .models import User as Profile


class ModelsTest(TestCase):
    def test_birthday_correct_birthday_today_in_context(self):
        response = Client().get("/")
        self.assertIn(
            "birthday_today",
            response.context,
        )

    def test_birthday_show_correct_context(self):
        self.user = Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday="2022-07-06"
        )
        self.user2 = Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday="2022-06-06"
        )
        response = Client().get("/")
        self.assertEqual(len(response.context["birthday_today"]), 0)

    def test_birthday_show_correct_context_not_null(self):
        self.user = Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday="2022-12-06"
        )
        self.user2 = Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday="2022-06-06"
        )
        response = Client().get("/")
        self.assertEqual(len(response.context["birthday_today"]), 1)

    def test_birthday_show_correct_context_not_null_name(self):
        self.user = Profile.objects.create_user(
            first_name="test1", email="test1@gmail.com", password="1234abcd",
            birthday="2022-12-06"
        )
        self.user2 = Profile.objects.create_user(
            first_name="test2", email="test2@gmail.com", password="1234abcd",
            birthday="2022-06-06"
        )
        response = Client().get("/")
        self.assertEqual(
            response.context["birthday_today"][0].email, "test1@gmail.com")
