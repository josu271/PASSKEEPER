from tkinter import *
from tkinter import messagebox

#Ventana del inicio
root = Tk()
root.title('Inicio de Sesion')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

#imagen
img = PhotoImage(file='../img/login.png')
Label(root, image=img, bg='#fff').place(x=50,y=50)

#Formulario
frame=Frame(root, width=350,height=380,bg="white")
frame.place(x=480,y=70)
heading=Label(frame, text='Registrar Usuario', fg='#57a1f8',bg='#fff', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=60,y=5)
#Correo
email = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
email.place(x=30, y=80)
email.insert(0, 'Correo Electronico')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#Usuario
user = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=125)
user.insert(0, 'Usuario')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=153)
#Contraseña
password = Entry(frame, width=25, fg='black', border=0, bg="#fff", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=170)
password.insert(0, 'Contraseña')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=198)
#Corfimacion
confirm = Entry(frame,width=25,fg='black', border=0,bg="#fff",font=('Microsoft YaHei UI Light',11))
confirm.place(x=30,y=215)
confirm.insert(0,'Confirmar Contraseña')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=245)
#boton
Button(frame,width=39,pady=7,text='Registrar',bg='#57a1f8',fg='#fff',border=0).place(x=35,y=260)
label=Label(frame,text="¿Ya tienes una cuenta?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label.place(x=80,y=305)
#Registrar
sign=Button(frame,width=10,text="Iniciar Sesion",border=0,bg='#fff',cursor='hand2', fg='#57a1f8')
sign.place(x=215,y=305)
root.mainloop()