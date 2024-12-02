from tkinter import *
from tkinter import messagebox
from src.database.tablePasskeeper import agregar_datos_passkeeper
import random
import string
class AgregarApp:
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent

        self.root.title("Agregar Contraseña")
        self.root.geometry("400x300+500+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # Formulario
        Label(root, text="Usuario", bg="#fff", font=("Arial", 10)).place(x=30, y=30)
        self.usuario_entry = Entry(root, width=30, font=("Arial", 10))
        self.usuario_entry.place(x=150, y=30)

        Label(root, text="Contraseña", bg="#fff", font=("Arial", 10)).place(x=30, y=70)
        self.contrasena_entry = Entry(root, width=30, font=("Arial", 10))
        self.contrasena_entry.place(x=150, y=70)

        # Botón para generar contraseña
        generar_button = Button(root, text="Generar", bg='#8E17EB', fg="white", font=("Arial", 10),
                                command=self.generar_contrasena)
        generar_button.place(x=320, y=70, width=70, height=25)

        Label(root, text="Sitio WEB", bg="#fff", font=("Arial", 10)).place(x=30, y=110)
        self.sitio_entry = Entry(root, width=30, font=("Arial", 10))
        self.sitio_entry.place(x=150, y=110)

        Label(root, text="Seguridad", bg="#fff", font=("Arial", 10)).place(x=30, y=150)
        self.seguridad_label = Label(root, text="", bg="#fff", font=("Arial", 10))
        self.seguridad_label.place(x=150, y=150)

        # Botón agregar
        agregar_button = Button(root, text="Agregar", bg='#8E17EB', fg="white", font=("Arial", 10, "bold"),
                                command=self.agregar_entrada)
        agregar_button.place(x=150, y=200, width=100, height=30)

        # Actualizar la seguridad de la contraseña automáticamente
        self.contrasena_entry.bind("<KeyRelease>", self.actualizar_seguridad)

    def generar_contrasena(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for _ in range(8))
        self.contrasena_entry.delete(0, 'end')  # Limpiar entrada
        self.contrasena_entry.insert('end', contrasena)  # Insertar nueva contraseña

    def actualizar_seguridad(self, event):
        contrasena = self.contrasena_entry.get()
        longitud = len(contrasena)

        if longitud < 3:
            seguridad = "Baja"
        elif 3 <= longitud <= 6:
            seguridad = "Media"
        else:
            seguridad = "Alta"

        self.seguridad_label.config(text=seguridad)

    def agregar_entrada(self):
        usuariox = self.parent.id_usuario
        usuarioPass = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        sitio = self.sitio_entry.get()
        seguridad = self.seguridad_label.cget("text")  # Obtener el texto actual de seguridad

        # Validar que todos los campos estén completos
        if not usuarioPass or not contrasena or not sitio:
            messagebox.showwarning("Formulario incompleto", "Por favor completa todos los campos.")
            return

        try:
            # Intentar agregar los datos a la base de datos
            agregar_datos_passkeeper(usuarioPass, contrasena, sitio, seguridad, id_user=usuariox)

            # Mensaje de éxito
            messagebox.showinfo("Éxito", "Se ha agregado exitosamente la contraseña")

            # Llamar al método agregar_entrada de la instancia padre (PasskeeperApp)
            if hasattr(self.parent, "agregar_entrada"):
                self.parent.agregar_entrada(usuarioPass, contrasena, sitio, seguridad)

            # Cerrar la ventana secundaria
            self.root.destroy()
        except Exception as e:
            # Manejo de errores
            messagebox.showerror("Error", f"No se pudieron agregar los datos: {e}")