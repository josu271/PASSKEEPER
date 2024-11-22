from tkinter import *
from tkinter import messagebox
from src.Logica.Ventana import Ventana


#Ventana del inicio
root = Tk()
root.title('Restablecer Contraseña')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

app_manager = Ventana(root)

#imagen
img = PhotoImage(file='../img/login.png')
Label(root, image=img, bg='#fff').place(x=50,y=50)

#Formulario
frame=Frame(root, width=400,height=400,bg="#fff")
frame.place(x=530,y=70)
heading=Label(frame, text='Restablecer Contraseña', fg='#57a1f8',bg='#fff', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=10,y=5)

#Usuario
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Usuario')
user = Entry(frame,width=25,fg='black', border=0,bg="#fff",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#Contraseña
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0,'Contraseña')
code = Entry(frame,width=25,fg='black', border=0,bg="#fff",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Contraseña')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
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
Button(frame,width=39,pady=7,text='Restablecer',bg='#57a1f8',fg='#fff',border=0, command=app_manager.abrir_inicio).place(x=35,y=260)
label=Label(frame,text="¿Tienes una cuenta?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label.place(x=70,y=300)
#Recupera
sign=Button(frame,width=10,text="Iniciar Sesion",border=0,bg='#fff',cursor='hand2', fg='#57a1f8', command=app_manager.abrir_inicio)
sign.place(x=215,y=300)

#Registrar
label2=Label(frame,text="¿Es tu primera ves?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label2.place(x=70,y=330)
sign=Button(frame,width=8,text="Registrate",border=0,bg='#fff',cursor='hand2', fg='#57a1f8', command=app_manager.abrir_registro)
sign.place(x=215,y=330)
root.mainloop()
