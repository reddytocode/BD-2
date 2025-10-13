from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserAccountModelTest(TestCase):
    """Tests para el modelo UserAccount"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="patient"
        )
    
    def test_user_creation(self):
        """Test de creación de usuario"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.role, "patient")
        self.assertFalse(self.user.is_verified)
    
    def test_user_str_representation(self):
        """Test de representación string del usuario"""
        expected = "testuser (Paciente)"
        self.assertEqual(str(self.user), expected)
    
    def test_full_name_property(self):
        """Test de la propiedad full_name"""
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()
        
        self.assertEqual(self.user.full_name, "John Doe")
    
    def test_full_name_without_names(self):
        """Test de full_name cuando no hay nombres"""
        self.assertEqual(self.user.full_name, "testuser")


class UserAccountAdminTest(TestCase):
    """Tests para el admin de UserAccount"""
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123"
        )
        self.client.login(username="admin", password="adminpass123")
    
    def test_admin_list_view(self):
        """Test de la vista de lista del admin"""
        response = self.client.get("/admin/accounts/useraccount/")
        self.assertEqual(response.status_code, 200)
    
    def test_admin_add_view(self):
        """Test de la vista de agregar usuario en admin"""
        response = self.client.get("/admin/accounts/useraccount/add/")
        self.assertEqual(response.status_code, 200)
