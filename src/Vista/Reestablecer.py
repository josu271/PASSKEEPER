from tkinter import *
from tkinter import messagebox
from src.database.Reestablecer import DBController
from src.Logica.Ventana import Ventana

# Crear instancia del controlador de base de datos
db = DBController()

# Ventana del restablecimiento de contraseña
root = Tk()
root.title('Restablecer Contraseña')
root.geometry('450x450+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Crear instancia de la clase Ventana
app_manager = Ventana(root)



# Formulario
frame = Frame(root, width=400, height=600, bg="#fff")
frame.place(x=50, y=20)


# Imagen
img = PhotoImage(file='../../Imagenes/img/login.png')
Label(frame, image=img, bg='#fff').place(x=70, y=20)
#Titulo
heading = Label(frame, text='Restablecer Contraseña', fg='#8e17eb', bg='#fff',
                font=('Microsoft YaHei UI Light', 23, 'bold'))  # Cambiar el color a púrpura
heading.place(x=10, y=5)

# Usuario
def on_enter_user(e):
    if user_entry.get() == "Usuario":
        user_entry.delete(0, 'end')


def on_leave_user(e):
    if not user_entry.get():
        user_entry.insert(0, 'Usuario')


user_entry = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
user_entry.place(x=30, y=200)
user_entry.insert(0, 'Usuario')
user_entry.bind('<FocusIn>', on_enter_user)
user_entry.bind('<FocusOut>', on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=225)


# Nueva contraseña
def on_enter_pass(e):
    if password_entry.get() == "Nueva Contraseña":
        password_entry.delete(0, 'end')
        password_entry.config(show="*")


def on_leave_pass(e):
    if not password_entry.get():
        password_entry.insert(0, 'Nueva Contraseña')
        password_entry.config(show="")


password_entry = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
password_entry.place(x=30, y=245)
password_entry.insert(0, 'Nueva Contraseña')
password_entry.bind('<FocusIn>', on_enter_pass)
password_entry.bind('<FocusOut>', on_leave_pass)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=270)


# Confirmar contraseña
def on_enter_confirm(e):
    if confirm_entry.get() == "Confirmar Contraseña":
        confirm_entry.delete(0, 'end')
        confirm_entry.config(show="*")


def on_leave_confirm(e):
    if not confirm_entry.get():
        confirm_entry.insert(0, 'Confirmar Contraseña')
        confirm_entry.config(show="")


confirm_entry = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
confirm_entry.place(x=30, y=285)
confirm_entry.insert(0, 'Confirmar Contraseña')
confirm_entry.bind('<FocusIn>', on_enter_confirm)
confirm_entry.bind('<FocusOut>', on_leave_confirm)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=310)


# Función para restablecer contraseña
def restablecer_contraseña():
    usuario = user_entry.get()
    nueva_contraseña = password_entry.get()
    confirmar_contraseña = confirm_entry.get()

    if not usuario or usuario == 'Usuario':
        messagebox.showerror("Error", "El campo de usuario no puede estar vacío.")
        return
    if nueva_contraseña != confirmar_contraseña:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return

    # Verificar si el usuario existe
    user = db.buscar_usuario(usuario)
    if not user:
        messagebox.showerror("Error", "Usuario no encontrado.")
        return

    # Actualizar la contraseña
    if db.actualizar_contraseña(usuario, nueva_contraseña):
        messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
    else:
        messagebox.showerror("Error", "No se pudo actualizar la contraseña.")



# Botón de restablecer
Button(frame, width=39, pady=7, text='Restablecer', bg='#8e17eb', fg='#fff', border=0,  # Cambiar el color a púrpura
       command=restablecer_contraseña).place(x=35, y=315)

# Botón de regresar a Inicio de Sesión
sign = Button(frame, width=25, text="Volver a inicio de sesion", border=0, bg='#fff', cursor='hand2', fg='#8e17eb',
              command=app_manager.abrir_inicio)
sign.place(x=80, y=355)

root.mainloop()
