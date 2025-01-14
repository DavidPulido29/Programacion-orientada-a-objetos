import tkinter as tk
from tkinter import ttk

class Comparador:
    def __init__(self, valor_a, valor_b):
        self.valor_a = float(valor_a)
        self.valor_b = float(valor_b)

    def comparar_valores(self):
        if self.valor_a > self.valor_b:
            return "A es mayor que B."
        elif self.valor_a < self.valor_b:
            return "A es menor que B."
        else:
            return "A es igual a B."

# Función para manejar la lógica de comparación
def comparar():
    try:
        valor_a = float(entry_valor_a.get())
        valor_b = float(entry_valor_b.get())
        comparador = Comparador(valor_a, valor_b)
        resultado = comparador.comparar_valores()
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, ingresa valores numéricos válidos.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Comparador de Valores")

# Creación de los widgets
label_valor_a = ttk.Label(root, text="Valor de A:")
label_valor_a.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_valor_a = ttk.Entry(root)
entry_valor_a.grid(row=0, column=1, padx=10, pady=5)

label_valor_b = ttk.Label(root, text="Valor de B:")
label_valor_b.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_valor_b = ttk.Entry(root)
entry_valor_b.grid(row=1, column=1, padx=10, pady=5)

button_comparar = ttk.Button(root, text="Comparar", command=comparar)
button_comparar.grid(row=2, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="", justify="center")
label_resultado.grid(row=3, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
