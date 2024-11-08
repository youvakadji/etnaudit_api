from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

class GeneralTests(TestCase):

    def setUp(self):
        """Préparation des données de test"""
        # Créez un utilisateur pour les tests avec un email obligatoire
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            password='password123', 
            email='testuser@example.com'
        )
        # Créez un autre utilisateur administrateur
        self.admin_user = get_user_model().objects.create_superuser(
            username='adminuser',
            email='adminuser@example.com',
            password='adminpassword123'
        )
        # URL de base pour un test général
        self.url = reverse('user-list')

    def test_user_creation(self):
        """Test la création d'un utilisateur"""
        email = 'newuser@example.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email, 
            password=password,
            username='newuser'
        )
        self.assertEqual(user.email, email.lower())  # Vérifier l'email normalisé
        self.assertTrue(user.check_password(password))  # Vérifier le mot de passe

    def test_user_permissions_authenticated(self):
        """Test l'accès aux vues pour un utilisateur authentifié"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # L'utilisateur authentifié doit avoir accès

    def test_admin_user_permissions(self):
        """Test les permissions de l'administrateur"""
        self.client.login(username='adminuser', password='adminpassword123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # L'administrateur doit avoir accès
