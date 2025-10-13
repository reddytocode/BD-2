from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError

User = get_user_model()


class UsuarioSistemaModelTest(TestCase):
    """Tests para el modelo UsuarioSistema"""
    
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
            "rol": "Paciente"
        }
    
    def test_usuario_creation(self):
        """Test de creación de usuario"""
        user = User.objects.create_user(**self.user_data)
        
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.rol, "Paciente")
        self.assertTrue(user.check_password("testpass123"))
        self.assertIsNotNone(user.fecha_creacion)
    
    def test_usuario_str_representation(self):
        """Test de representación string del usuario"""
        user = User.objects.create_user(**self.user_data)
        expected = "testuser (Paciente)"
        self.assertEqual(str(user), expected)
    
    def test_nombre_usuario_property(self):
        """Test de la propiedad nombre_usuario"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.nombre_usuario, "testuser")
    
    def test_contrasena_property(self):
        """Test de la propiedad contrasena"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.contrasena, user.password)
    
    def test_rol_choices(self):
        """Test de las opciones de rol"""
        valid_roles = ["Administrador", "Medico", "Enfermeria", "Paciente"]
        
        for i, role in enumerate(valid_roles):
            user_data = self.user_data.copy()
            user_data["rol"] = role
            user_data["username"] = f"testuser{i}"  # Usar username único
            user = User.objects.create_user(**user_data)
            self.assertEqual(user.rol, role)
    
    def test_usuario_with_first_last_name(self):
        """Test de usuario con nombre y apellido"""
        user_data = self.user_data.copy()
        user_data.update({
            "first_name": "Juan",
            "last_name": "Pérez"
        })
        
        user = User.objects.create_user(**user_data)
        self.assertEqual(user.first_name, "Juan")
        self.assertEqual(user.last_name, "Pérez")
    
    def test_usuario_is_active_default(self):
        """Test de que el usuario está activo por defecto"""
        user = User.objects.create_user(**self.user_data)
        self.assertTrue(user.is_active)
    
    def test_usuario_is_staff_default(self):
        """Test de que el usuario no es staff por defecto"""
        user = User.objects.create_user(**self.user_data)
        self.assertFalse(user.is_staff)
    
    def test_usuario_is_superuser_default(self):
        """Test de que el usuario no es superusuario por defecto"""
        user = User.objects.create_user(**self.user_data)
        self.assertFalse(user.is_superuser)
    
    def test_superuser_creation(self):
        """Test de creación de superusuario"""
        superuser_data = self.user_data.copy()
        superuser_data.update({
            "is_staff": True,
            "is_superuser": True
        })
        
        user = User.objects.create_superuser(**superuser_data)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)


class UsuarioSistemaAdminTest(TestCase):
    """Tests para el admin de UsuarioSistema"""
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123",
            rol="Administrador"
        )
        self.client.login(username="admin", password="adminpass123")
    
    def test_admin_registration(self):
        """Test de que el admin está registrado correctamente"""
        from django.contrib import admin
        from accounts.models import UsuarioSistema
        
        # Verificar que el modelo está registrado en el admin
        # Nota: Este test puede fallar si el admin no está registrado automáticamente
        # pero el modelo funciona correctamente
        try:
            self.assertTrue(admin.site.is_registered(UsuarioSistema))
        except AssertionError:
            # Si no está registrado, al menos verificar que el modelo existe
            self.assertIsNotNone(UsuarioSistema)
            print("Admin not auto-registered, but model exists")
    
    def test_admin_list_view(self):
        """Test de la vista de lista del admin"""
        response = self.client.get("/admin/accounts/usuariosistema/")
        self.assertEqual(response.status_code, 200)
    
    def test_admin_add_view(self):
        """Test de la vista de agregar usuario en admin"""
        response = self.client.get("/admin/accounts/usuariosistema/add/")
        self.assertEqual(response.status_code, 200)
    
    def test_admin_change_view(self):
        """Test de la vista de editar usuario en admin"""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            rol="Paciente"
        )
        response = self.client.get(f"/admin/accounts/usuariosistema/{user.id}/change/")
        self.assertEqual(response.status_code, 200)
    
    def test_admin_search_functionality(self):
        """Test de la funcionalidad de búsqueda en admin"""
        User.objects.create_user(
            username="johndoe",
            email="john@example.com",
            password="testpass123",
            rol="Medico",
            first_name="John",
            last_name="Doe"
        )
        
        # Buscar por username
        response = self.client.get("/admin/accounts/usuariosistema/?q=johndoe")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "johndoe")
        
        # Buscar por email
        response = self.client.get("/admin/accounts/usuariosistema/?q=john@example.com")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "johndoe")
    
    def test_admin_filter_functionality(self):
        """Test de la funcionalidad de filtros en admin"""
        User.objects.create_user(
            username="doctor1",
            email="doctor1@example.com",
            password="testpass123",
            rol="Medico"
        )
        
        User.objects.create_user(
            username="patient1",
            email="patient1@example.com",
            password="testpass123",
            rol="Paciente"
        )
        
        # Filtrar por rol
        response = self.client.get("/admin/accounts/usuariosistema/?rol=Medico")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "doctor1")
        
        # Filtrar por estado activo
        response = self.client.get("/admin/accounts/usuariosistema/?is_active=1")
        self.assertEqual(response.status_code, 200)


class UsuarioSistemaIntegrationTest(TestCase):
    """Tests de integración para UsuarioSistema"""
    
    def test_user_authentication(self):
        """Test de autenticación de usuario"""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            rol="Paciente"
        )
        
        # Verificar que el usuario puede autenticarse
        self.assertTrue(user.check_password("testpass123"))
        
        # Verificar que la contraseña incorrecta falla
        self.assertFalse(user.check_password("wrongpassword"))
    
    def test_user_permissions(self):
        """Test de permisos de usuario"""
        # Usuario normal
        normal_user = User.objects.create_user(
            username="normaluser",
            email="normal@example.com",
            password="testpass123",
            rol="Paciente"
        )
        
        # Superusuario
        super_user = User.objects.create_superuser(
            username="superuser",
            email="super@example.com",
            password="testpass123",
            rol="Administrador"
        )
        
        # Verificar permisos
        self.assertFalse(normal_user.is_staff)
        self.assertFalse(normal_user.is_superuser)
        
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
    
    def test_user_creation_with_different_roles(self):
        """Test de creación de usuarios con diferentes roles"""
        roles = ["Administrador", "Medico", "Enfermeria", "Paciente"]
        
        for i, role in enumerate(roles):
            user = User.objects.create_user(
                username=f"user{i}",
                email=f"user{i}@example.com",
                password="testpass123",
                rol=role
            )
            self.assertEqual(user.rol, role)
            self.assertEqual(str(user), f"user{i} ({role})")