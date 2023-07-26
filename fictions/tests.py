from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Fiction
# Create your tests here.
class FictionTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_thing = Fiction.objects.create(
            name="Matrix",
            owner=testuser1,
            gener="Action.",
        )
        test_thing.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_fictions_model(self):
        fiction = Fiction.objects.get(id=1)
        actual_owner = str(fiction.owner)
        actual_name = str(fiction.name)
        actual_gener = str(fiction.gener)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Matrix")
        self.assertEqual(
            actual_gener, "Action."
        )

    def test_get_fiction_list(self):
        url = reverse("fiction_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        fictions = response.data
        self.assertEqual(len(fictions), 1)
        self.assertEqual(fictions[0]["name"], "Matrix")


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