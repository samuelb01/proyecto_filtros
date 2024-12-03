import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from filters import thirdOctaveFilter, octaveFilter  # Importar las funciones necesarias



# Configuración principal de la ventana
root = tk.Tk()
root.title("Ecualizador Gráfico")

#  Variables
file_entry = tk.StringVar()
selected_filter = tk.StringVar(value="Tercio de octava")

# Menú para seleccionar bandas
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Submenús que se asocian luego al menú principal
menu_file = tk.Menu(menu_bar, tearoff=0)


first_band = tk.StringVar(value="25")
last_band = tk.StringVar(value="2000")

# Bucle principal de la aplicación
root.mainloop()