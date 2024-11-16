from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('Passkeeper')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="#fff")
root.resizable(True, True)
#imagen
img = PhotoImage(file='../img/logo.png')
Label(root, image=img, bg='#fff').place(x=900,y=-45)
# Contenido principal
shadow = Frame(root, width=350, bg="#d9d9d9")
shadow.place(x=5, y=5, relheight=1)
conten = Frame(root, width=350, bg="#fff", highlightbackground="#ccc", highlightthickness=1)
conten.place(x=0, y=0, relheight=1)
label = Label(conten, text="PASSKEEPER", fg='Black', bg='#fff', font=('Arial', 20, 'bold'))
label.place(x=80, y=30)

agregar = tk.Button(conten, text="AGREGAR", bg='#57a1f8', fg="white", font=("Arial", 10, "bold"))
agregar.place(relx=0, rely=0.15, relwidth=1, height=50)
config = tk.Button(conten, text="CONFIGURACIÓN", bg='#57a1f8', fg="white", font=("Arial", 10, "bold"))
config.place(relx=0, rely=0.22, relwidth=1, height=50)

# Búsqueda
look = Frame(root, width=500, height=100, bg="#fff", highlightbackground="#fff", highlightthickness=0)
look.place(relx=0.5, rely=0.06, anchor=N)

barra = Entry(look, width=35, fg='black', bg="#f2f2f2", font=('Microsoft YaHei UI Light', 12), bd=0, highlightbackground="#57a1f8", highlightthickness=1)
barra.place(relx=0.05, rely=0.2, relwidth=0.7, height=40)

buscar = Button(look, text="Buscar", bg='#57a1f8', fg="white", font=("Arial", 12, "bold"), bd=0, activebackground="#005cbf", activeforeground="white", cursor="hand2")
buscar.place(relx=0.78, rely=0.2, relwidth=0.2, height=40)


# Tabla
ftable = Frame(root, width=1400, height=800, bg="#fff")
ftable.place(x=425, y=150, relwidth=0.7, relheight=0.7)

# Configuración de estilo para mejorar apariencia de la tabla
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                font=('Arial', 12)  ,
                rowheight=25,
                background="#f9f9f9",
                foreground="#000")
style.configure("Treeview.Heading",
                font=('Arial', 12, 'bold'),
                background="#57a1f8",
                foreground="black")
style.map("Treeview",
          background=[('selected', '#005cbf')],
          foreground=[('selected', 'black')])

tabla = ttk.Treeview(ftable, columns=("Usuario", "Contraseña", "Sitio WEB", "Seguridad", "Acciones"), show="headings")
tabla.heading("Usuario", text="Usuario")
tabla.heading("Contraseña", text="Contraseña")
tabla.heading("Sitio WEB", text="Sitio WEB")
tabla.heading("Seguridad", text="Seguridad")
tabla.heading("Acciones", text="Acciones")
tabla.column("Usuario", anchor="center")
tabla.column("Contraseña", anchor="center")
tabla.column("Sitio WEB", anchor="center")
tabla.column("Seguridad", anchor="center")
tabla.column("Acciones", anchor="center")

style.configure("Horizontal.TScrollbar",
                background="white",
                troughcolor="white",
                bordercolor="white",
                arrowcolor="black")
style.configure("Vertical.TScrollbar",
                background="white",
                troughcolor="white",
                bordercolor="white",
                arrowcolor="black")

scroll_x = ttk.Scrollbar(ftable, orient=HORIZONTAL, command=tabla.xview, style="Horizontal.TScrollbar")
scroll_y = ttk.Scrollbar(ftable, orient=VERTICAL, command=tabla.yview, style="Vertical.TScrollbar")

tabla.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
tabla.pack(fill=BOTH, expand=True)

root.mainloop()
