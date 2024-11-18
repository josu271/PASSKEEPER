# gestor/app_manager.py
import subprocess

class Ventana:
    def __init__(self, root):
        self.root = root

    def abrir_passkeeper(self):
        self.root.destroy()
        subprocess.run(["python", "Form/Passkeeper.py"])

    def abrir_reestablecer(self):
        self.root.destroy()
        subprocess.run(["python", "Form/Reestablecer.py"])

    def abrir_registro(self):
        self.root.destroy()
        subprocess.run(["python", "Form/Registro_Usuario.py"])
