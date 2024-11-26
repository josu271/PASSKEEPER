from tkinter import *
from tkinter import messagebox


class EditarApp:
    def __init__(self, root, parent, valores):
        self.root = root
        self.parent = parent  # La referencia a la instancia de PasskeeperApp
        self.valores = valores  # Los valores actuales del elemento seleccionado

        self.root.title("Editar Contraseña")
        self.root.geometry("400x300")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # Formulario
        Label(root, text="Usuario", bg="#fff", font=("Arial", 10)).place(x=30, y=30)
        self.usuario_entry = Entry(root, width=30, font=("Arial", 10))
        self.usuario_entry.place(x=150, y=30)
        self.usuario_entry.insert(0, valores[0])

        Label(root, text="Contraseña", bg="#fff", font=("Arial", 10)).place(x=30, y=70)
        self.contrasena_entry = Entry(root, width=30, font=("Arial", 10))
        self.contrasena_entry.place(x=150, y=70)
        self.contrasena_entry.insert(0, valores[1])

        Label(root, text="Sitio WEB", bg="#fff", font=("Arial", 10)).place(x=30, y=110)
        self.sitio_entry = Entry(root, width=30, font=("Arial", 10))
        self.sitio_entry.place(x=150, y=110)
        self.sitio_entry.insert(0, valores[2])

        Label(root, text="Seguridad", bg="#fff", font=("Arial", 10)).place(x=30, y=150)
        self.seguridad_label = Label(root, text=valores[3], bg="#fff", font=("Arial", 10))
        self.seguridad_label.place(x=150, y=150)

        # Botón editar
        editar_button = Button(root, text="Guardar", bg='#8E17EB', fg="white", font=("Arial", 10, "bold"),
                               command=self.guardar_cambios)
        editar_button.place(x=150, y=200, width=100, height=30)

        # Actualizar la seguridad de la contraseña automáticamente
        self.contrasena_entry.bind("<KeyRelease>", self.actualizar_seguridad)

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

    def guardar_cambios(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        sitio = self.sitio_entry.get()
        seguridad = self.seguridad_label.cget("text")

        # Validar que todos los campos estén completos
        if not usuario or not contrasena or not sitio:
            messagebox.showwarning("Formulario incompleto", "Por favor completa todos los campos.")
            return

        # Actualiza la tabla en la instancia original
        seleccion = self.parent.tabla.selection()
        if seleccion:
            for item in seleccion:
                self.parent.tabla.item(item, values=(usuario, contrasena, sitio, seguridad))

        # Cerrar la ventana secundaria
        self.root.destroy()