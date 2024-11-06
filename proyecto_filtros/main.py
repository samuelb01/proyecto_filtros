# TFG FILTROS
# SAMUEL BELLÓN ELIPE


# Modulos
import tkinter as tk
from tkinter import filedialog

# Clase aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title = "Ecualizador"

    def printHolaMundo(self):
        print("Hola Mundo")


def main():
    root = tk.Tk
    app = App(root)
    app.printHolaMundo()

# Código principal para iniciar la aplicación
if __name__ == "__main__":
    main()