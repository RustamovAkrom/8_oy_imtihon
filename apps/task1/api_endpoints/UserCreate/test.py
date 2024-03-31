from django.test import TestCase
from apps.task1.models import User
from django.urls import reverse


class TestUserCreate(TestCase):
    def setUp(self):
        self.url = reverse("task1:user-create")

    def test_create(self):
        response = self.client.get(self.url)
        print(response.json())
        print(response.status_code)
