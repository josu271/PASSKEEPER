import sqlite3

try:
    # Conexión a la base de datos
    mi_conexion = sqlite3.connect("BDpasskeeper.db")  # Asegúrate de agregar la extensión .db
    mi_conexion.execute("PRAGMA foreign_keys = 1")  # Habilitar soporte para claves foráneas
    cursor = mi_conexion.cursor()

    # Crear la tabla USUARIO
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        IDUser INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(200),
        Contraseña VARCHAR(200),
        Correo VARCHAR(200)
    )
    """)

    # Crear la tabla PassKeeper con la relación hacia USUARIO
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PassKeeper (
        IDPasskeeper INTEGER PRIMARY KEY AUTOINCREMENT,
        Usuario_Pass VARCHAR(200),
        Contraseña_Pass VARCHAR(200),
        SitioWeb VARCHAR(200),
        Seguridad VARCHAR(50),
        IDUser INTEGER,
        FOREIGN KEY(IDUser) REFERENCES usuario(IDUser) ON DELETE CASCADE
    )
    """)

    # Confirmar cambios
    mi_conexion.commit()
    print("Tablas creadas con éxito")

except Exception as ex:
    print("Ocurrió un error:", ex)