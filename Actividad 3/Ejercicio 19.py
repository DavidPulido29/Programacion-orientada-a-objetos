import tkinter as tk
from tkinter import ttk
import math


class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = float(lado)

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def mostrar_resultados(self):
        perimetro = self.calcular_perimetro()
        altura = self.calcular_altura()
        area = self.calcular_area()
        return perimetro, altura, area


def calcular():
    try:
        lado = float(entry_lado.get())
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        triangulo = TrianguloEquilatero(lado)
        perimetro, altura, area = triangulo.mostrar_resultados()
        label_resultado.config(
            text=(
                f"Perímetro del triángulo: {perimetro:.2f}\n"
                f"Altura del triángulo: {altura:.2f}\n"
                f"Área del triángulo: {area:.2f}"
            )
        )
    except ValueError as e:
        label_resultado.config(text=f"Error: {e}")


# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Triángulo Equilátero")

# Creación de los widgets
label_lado = ttk.Label(root, text="Valor del lado del triángulo equilátero:")
label_lado.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_lado = ttk.Entry(root)
entry_lado.grid(row=0, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=1, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="", justify="left")
label_resultado.grid(row=2, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
