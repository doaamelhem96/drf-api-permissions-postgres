from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from .models import Fiction

class FictionAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )

        test_fiction = Fiction.objects.create(
            owner=testuser1,
            name="rake",
            gener="Better for collecting leaves than a shovel.",  # Updated field name to 'gener'
        )

    def setUp(self) -> None:
        self.client.login(username="testuser1", password="pass")  

    def test_fictions_model(self):
        thing = Fiction.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_gener = str(thing.gener)  # Updated field name to 'gener'
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_gener, "Better for collecting leaves than a shovel."
        )
    def test_get_fictions_list(self):
        url = reverse("fiction_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["name"], "rake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("fiction_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete_fiction(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("fiction_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
