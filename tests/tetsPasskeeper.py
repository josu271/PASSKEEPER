import unittest
from unittest.mock import MagicMock, patch
from src.database.inicio import verificar_credenciales
from tkinter import Tk
from src.Vista.Agregar import AgregarApp
class PruebasPassKeeper(unittest.TestCase):

    def test_usuario_incorrecto(self):
        usuario = "invalido"
        contrasena = "1234"
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Usuario incorrecto debería retornar False.")

    def test_contrasena_incorrecta(self):
        usuario = "admin"
        contrasena = "wrongpassword"
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Contraseña incorrecta debería retornar False.")

    def test_usuario_y_contrasena_incorrectos(self):
        usuario = "wronguser"
        contrasena = "wrongpassword"
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Usuario y contraseña incorrectos deberían retornar False.")

    def test_caracteres_especiales(self):
        usuario = "admin"
        contrasena = "1234' OR '1'='1"
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Inyección de SQL debería retornar False.")

    def test_credenciales_incorrectas(self):
        usuario = "123"
        contrasena = "222"
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Credenciales incorrectas deberían retornar False.")

    def test_campos_vacios(self):
        usuario = ""
        contrasena = ""
        resultado = verificar_credenciales(usuario, contrasena)
        self.assertFalse(resultado, "Campos vacíos deberían retornar False.")

    def setUp(self):
        # Crear un objeto Tk para la prueba
        self.root = Tk()
        self.parent_mock = MagicMock()
        self.parent_mock.id_usuario = 1
        self.app = AgregarApp(self.root, self.parent_mock)

    def tearDown(self):
        self.root.destroy()

    def test_generar_contrasena(self):
        # Verificar que se genera una contraseña de 8 caracteres
        self.app.generar_contrasena()
        contrasena = self.app.contrasena_entry.get()
        self.assertEqual(len(contrasena), 8, "La contraseña generada debería tener 8 caracteres.")

    def test_actualizar_seguridad_baja(self):
        # Simular una contraseña de baja seguridad
        self.app.contrasena_entry.insert(0, "12")
        self.app.actualizar_seguridad(None)
        seguridad = self.app.seguridad_label.cget("text")
        self.assertEqual(seguridad, "Baja", "Una contraseña corta debería mostrar seguridad 'Baja'.")

    def test_actualizar_seguridad_media(self):
        # Simular una contraseña de seguridad media
        self.app.contrasena_entry.insert(0, "123456")
        self.app.actualizar_seguridad(None)
        seguridad = self.app.seguridad_label.cget("text")
        self.assertEqual(seguridad, "Media", "Una contraseña de longitud media debería mostrar seguridad 'Media'.")

    def test_actualizar_seguridad_alta(self):
        # Simular una contraseña de alta seguridad
        self.app.contrasena_entry.insert(0, "123456789")
        self.app.actualizar_seguridad(None)
        seguridad = self.app.seguridad_label.cget("text")
        self.assertEqual(seguridad, "Alta", "Una contraseña larga debería mostrar seguridad 'Alta'.")
if __name__ == '__main__':
    unittest.main()
