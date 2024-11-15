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
frame=Frame(root, width=350,height=350,bg="#fff")
frame.place(x=480,y=70)
heading=Label(frame, text='Iniciar Sesión', fg='#57a1f8',bg='#fff', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

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
#boton
Button(frame,width=39,pady=7,text='Ingresar',bg='#57a1f8',fg='#fff',border=0).place(x=35,y=204)
label=Label(frame,text="¿Olvidaste tu contraseña?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label.place(x=70,y=270)
#Recuperar
sign=Button(frame,width=8,text="Recuperar",border=0,bg='#fff',cursor='hand2', fg='#57a1f8')
sign.place(x=215,y=270)

#Registrar
label2=Label(frame,text="¿Es tu primera ves?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
label2.place(x=70,y=290)
sign=Button(frame,width=8,text="Registrate",border=0,bg='#fff',cursor='hand2', fg='#57a1f8')
sign.place(x=215,y=290)
root.mainloop()
