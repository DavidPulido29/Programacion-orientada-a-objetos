import tkinter as tk
from tkinter import ttk
import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz_discriminante = math.sqrt(discriminante)
            solucion1 = (-self.b + raiz_discriminante) / (2 * self.a)
            solucion2 = (-self.b - raiz_discriminante) / (2 * self.a)
            return solucion1, solucion2
        elif discriminante == 0:
            solucion_unica = -self.b / (2 * self.a)
            return solucion_unica,
        else:
            return "No tiene soluciones reales."

# Función para configurar la interfaz gráfica
def calcular():
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    ecuacion = EcuacionSegundoGrado(a, b, c)
    soluciones = ecuacion.calcular_soluciones()
    
    if isinstance(soluciones, str):
        label_resultado.config(text=soluciones)
    else:
        resultado_texto = "Soluciones de la ecuación de segundo grado:\n"
        for solucion in soluciones:
            resultado_texto += f"{solucion}\n"
        label_resultado.config(text=resultado_texto)

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Ecuaciones de Segundo Grado")

# Creación de los widgets
label_a = ttk.Label(root, text="Coeficiente A:")
label_a.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_a = ttk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = ttk.Label(root, text="Coeficiente B:")
label_b.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_b = ttk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

label_c = ttk.Label(root, text="Coeficiente C:")
label_c.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_c = ttk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=3, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
