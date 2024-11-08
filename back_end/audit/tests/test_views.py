from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

class UserViewTests(TestCase):

    def setUp(self):
        # Créez un utilisateur pour les tests, avec un email obligatoire
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            password='password123', 
            email='testuser@example.com'  # Ajoutez un email
        )
        self.url = reverse('user-list')  # L'URL de la vue UserListView

    def test_user_list_view_status_code(self):
        # Tester si la réponse de la vue est correcte (code 200)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Vérifie que le code de réponse est 200

    def test_user_list_view_json(self):
        # Tester si la réponse est bien en JSON
        response = self.client.get(self.url)
        self.assertEqual(response['Content-Type'], 'application/json')  # Vérifie que la réponse est en JSON

        # Vérifiez que la réponse contient des utilisateurs
        response_data = response.json()
        self.assertIsInstance(response_data, list)  # La réponse doit être une liste
        self.assertGreater(len(response_data), 0)  # Il doit y avoir au moins un utilisateur dans la réponse

    def test_user_list_view_empty(self):
        # Tester si la liste est vide quand il n'y a pas d'utilisateur
        get_user_model().objects.all().delete()  # Supprimer tous les utilisateurs
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Toujours 200
        response_data = response.json()
        self.assertEqual(len(response_data), 0)  # Aucune donnée dans la réponse
