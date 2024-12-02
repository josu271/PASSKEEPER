import sqlite3
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "BDpasskeeper.db"))


def obtener_conexion():
    """Establece una conexión con la base de datos."""
    try:
        conexion = sqlite3.connect(DB_PATH)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


def agregar_datos_passkeeper(usuario_pass, contraseña_pass, sitio_web, seguridad, id_user):
    try:
        conexion = obtener_conexion()
        if not conexion:
            return False  # No se pudo conectar a la base de datos
        cursor = conexion.cursor()
        query = """
        INSERT INTO PassKeeper (Usuario_Pass, Contraseña_Pass, SitioWeb, Seguridad, IDUser)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (usuario_pass, contraseña_pass, sitio_web, seguridad, id_user))
        conexion.commit()
        conexion.close()
        print("Datos agregados correctamente a PassKeeper.")
        return True
    except sqlite3.Error as e:
        print(f"Error al agregar datos a PassKeeper: {e}")
        return False


def actualizar_datos_passkeeper(usuario_pass, id_user, contraseña_pass=None, sitio_web=None):
    try:
        conexion = obtener_conexion()
        if not conexion:
            return False  # No se pudo conectar a la base de datos
        cursor = conexion.cursor()

        # Buscar el IDPasskeeper basado en usuario_pass y id_user
        cursor.execute("SELECT IDPasskeeper FROM PassKeeper WHERE Usuario_Pass = ? AND IDUser = ?", (usuario_pass, id_user))
        resultado = cursor.fetchone()

        # Si no se encuentra el registro, retornamos False
        if not resultado:
            print(f"No se encontró un registro con Usuario_Pass '{usuario_pass}' y IDUser '{id_user}'.")
            return False

        id_passkeeper = resultado[0]  # El IDPasskeeper del registro encontrado

        # Crear la consulta dinámica para incluir solo los campos que se desean actualizar
        campos_a_actualizar = []
        valores = []

        # Solo actualizamos los campos que se pasan como parámetros
        if contraseña_pass:
            campos_a_actualizar.append("Contraseña_Pass = ?")
            valores.append(contraseña_pass)
        if sitio_web:
            campos_a_actualizar.append("SitioWeb = ?")
            valores.append(sitio_web)

        # Verificar si hay campos para actualizar
        if not campos_a_actualizar:
            print("No se proporcionaron campos para actualizar.")
            return False  # No se actualizará si no hay campos a cambiar

        # Añadir el IDPasskeeper al final de los valores
        valores.append(id_passkeeper)

        # Construir y ejecutar la consulta de actualización
        query = f"UPDATE PassKeeper SET {', '.join(campos_a_actualizar)} WHERE IDPasskeeper = ?"
        cursor.execute(query, valores)
        conexion.commit()
        conexion.close()

        if cursor.rowcount > 0:
            print(f"Registro con IDPasskeeper {id_passkeeper} actualizado correctamente.")
            return True  # Indica que se actualizó correctamente
        else:
            print(f"No se encontró ningún registro con IDPasskeeper {id_passkeeper} para actualizar.")
            return False  # No se encontró el registro
    except sqlite3.Error as e:
        print(f"Error al actualizar datos en PassKeeper: {e}")
        return False



def obtener_datos_passkeeper(id_usuario):

    try:
        conexion = obtener_conexion()
        if not conexion:
            return []

        cursor = conexion.cursor()
        query = """
        SELECT Usuario_Pass, Contraseña_Pass, SitioWeb, Seguridad 
        FROM PassKeeper 
        WHERE IDUser = ?
        """
        cursor.execute(query, (id_usuario,))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except sqlite3.Error as e:
        print(f"Error al obtener los datos: {e}")
        return []
def eliminar_datos_passkeeper(id_usuario, usuario_pass, sitio_web):
    """
    Elimina un registro de la tabla PassKeeper basado en el usuario y sitio web.
    """
    try:
        conexion = obtener_conexion()
        if not conexion:
            return False

        cursor = conexion.cursor()
        query = """
        DELETE FROM PassKeeper
        WHERE IDUser = ? AND Usuario_Pass = ? AND SitioWeb = ?
        """
        cursor.execute(query, (id_usuario, usuario_pass, sitio_web))
        conexion.commit()

        if cursor.rowcount > 0:
            print(f"Registro eliminado correctamente: Usuario={usuario_pass}, Sitio={sitio_web}")
            return True
        else:
            print("No se encontró un registro para eliminar.")
            return False
    except sqlite3.Error as e:
        print(f"Error al eliminar los datos: {e}")
        return False
def actualizar_datos_passkeeper(id_usuario, usuario, contrasena, nuevo_sitio, seguridad, antiguo_sitio):
    """
    Actualiza los datos de un registro en la tabla PassKeeper.
    """
    try:
        conexion = obtener_conexion()
        if not conexion:
            return False

        cursor = conexion.cursor()

        # Consulta para actualizar
        consulta = """
            UPDATE PassKeeper 
            SET Usuario_Pass = ?, Contraseña_Pass = ?, SitioWeb = ?, Seguridad = ?
            WHERE IDUser = ? AND SitioWeb = ?;
        """
        # Ejecutar la consulta con el antiguo sitio como condición
        cursor.execute(consulta, (usuario, contrasena, nuevo_sitio, seguridad, id_usuario, antiguo_sitio))
        conexion.commit()

        # Confirmar si se actualizó alguna fila
        if cursor.rowcount > 0:
            print("Datos actualizados correctamente.")
            return True
        else:
            print("No se encontró un registro que coincida.")
            return False
    except sqlite3.Error as e:
        print(f"Error al actualizar los datos: {e}")
        return False

    finally:
        conexion.close()




