from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

class UserModelTests(TestCase):
    
    def test_create_user(self):
        # Test de création d'un utilisateur avec des informations valides
        user = get_user_model().objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='password123'
        )
        
        # Vérification que les données sont bien enregistrées
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        
        # Vérification du mot de passe crypté (assurez-vous que le mot de passe est bien crypté)
        self.assertTrue(user.check_password('password123'))
        
    def test_unique_email_constraint(self):
        # Test de la contrainte d'unicité de l'email
        get_user_model().objects.create_user(
            username='testuser1', 
            email='testuser@example.com', 
            password='password123'
        )
        
        # Tentative de création d'un utilisateur avec le même email
        with self.assertRaises(IntegrityError):  # L'email doit être unique
            get_user_model().objects.create_user(
                username='testuser2', 
                email='testuser@example.com', 
                password='password123'
            )
    
    def test_user_str_method(self):
        # Test de la méthode __str__() du modèle User
        user = get_user_model().objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='password123'
        )
        
        # Vérification que la méthode __str__() renvoie bien le username
        self.assertEqual(str(user), 'testuser')
