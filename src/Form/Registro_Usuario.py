from tkinter import *
from tkinter import messagebox
from src.Logica.Ventana import Ventana

#Ventana del inicio
root = Tk()
root.title('Registro de Usuario')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

app_manager = Ventana(root)

#imagen
img = PhotoImage(file='../img/login.png')
Label(root, image=img, bg='#fff').place(x=50,y=50)

#Formulario
frame=Frame(root, width=350,height=380,bg="white")
frame.place(x=480,y=70)
heading=Label(frame, text='Registrar Usuario', fg='#57a1f8',bg='#fff', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=60,y=5)
#Correo
def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    name = email.get()
    if name=='':
        email.insert(0,'Correo Electronico')
email = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
email.place(x=30, y=80)
email.insert(0, 'Correo Electronico')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#Usuario
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Usuario')
user = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=125)
user.insert(0, 'Usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=153)
#Contraseña
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name = password.get()
    if name=='':
        password.insert(0,'Usuario')
password = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=170)
password.insert(0, 'Contraseña')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=198)
#Corfimacion
def on_enter(e):
    confirm.delete(0,'end')
def on_leave(e):
    name = confirm.get()
    if name=='':
        confirm.insert(0,'Usuario')
confirm = Entry(frame,width=25,fg='black', border=0,bg="#fff",font=('Microsoft YaHei UI Light',11))
confirm.place(x=30,y=215)
confirm.insert(0,'Confirmar Contraseña')
confirm.bind('<FocusIn>', on_enter)
confirm.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=245)
#boton
Button(frame,width=39,pady=7,text='Registrar',bg='#57a1f8',fg='#fff',border=0, command=app_manager.abrir_inicio).place(x=35,y=260)
label=Label(frame,text="¿Ya tienes una cuenta?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label.place(x=80,y=305)
#Registrar
sign=Button(frame,width=10,text="Iniciar Sesion",border=0,bg='#fff',cursor='hand2', fg='#57a1f8', command=app_manager.abrir_inicio)
sign.place(x=215,y=305)
root.mainloop()