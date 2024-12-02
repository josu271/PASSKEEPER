import unittest
from src.database.inicio import verificar_credenciales

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

if __name__ == '__main__':
    unittest.main()
