from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from account.factories import UserFactory
from account.models import User


class UserCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.password = "parol123"
        self.user = UserFactory.build()

    def test_signup(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        user = User.objects.filter(email=self.user.email).first()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(self.password))
        self.assertEqual(res.data["email"], self.user.email)
        self.assertFalse("password" in res.data)
        self.assertFalse("conf_password" in res.data)

    def test_signup_without_conf_password(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_conf_password(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": self.password,
                "conf_password": "",
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_wrong_conf_password(self):
        WRONG_CONF_PASSWORD = self.password + "123"
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": self.password,
                "conf_password": WRONG_CONF_PASSWORD,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_without_password(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_password(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": "",
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_wrong_password(self):
        SHORT_PASSWORD = "test"
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "username": self.user.username,
                "password": SHORT_PASSWORD,
                "conf_password": SHORT_PASSWORD,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("password" in res.data)

    def test_signup_wrong_email(self):
        WRONG_EMAIL = "test"
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": WRONG_EMAIL,
                "username": self.user.username,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("email" in res.data)

    def test_signup_empty_email(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": "",
                "username": self.user.username,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("email" in res.data)

    def test_signup_without_email(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "username": self.user.username,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("email" in res.data)

    def test_signup_wrong_username(self):
        WRONG_USERNAME = "test~"
        res = self.client.post(
            reverse("account:signup"),
            {
                "username": WRONG_USERNAME,
                "email": self.user.email,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("username" in res.data)

    def test_signup_empty_username(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "username": "",
                "email": self.user.email,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("username" in res.data)

    def test_signup_without_username(self):
        res = self.client.post(
            reverse("account:signup"),
            {
                "email": self.user.email,
                "password": self.password,
                "conf_password": self.password,
            },
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("username" in res.data)
