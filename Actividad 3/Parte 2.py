import tkinter as tk
from tkinter import ttk
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"

# Función para configurar la interfaz gráfica
def calcular():
    tipo_figura = combo_tipo_figura.get()
    if tipo_figura == "Círculo":
        radio = float(entry_param1.get())
        figura = Circulo(radio)
        area = figura.calcular_area()
        perimetro = figura.calcular_perimetro()
        resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"
    elif tipo_figura == "Rectángulo":
        base = float(entry_param1.get())
        altura = float(entry_param2.get())
        figura = Rectangulo(base, altura)
        area = figura.calcular_area()
        perimetro = figura.calcular_perimetro()
        resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"
    elif tipo_figura == "Cuadrado":
        lado = float(entry_param1.get())
        figura = Cuadrado(lado)
        area = figura.calcular_area()
        perimetro = figura.calcular_perimetro()
        resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"
    elif tipo_figura == "Triángulo Rectángulo":
        base = float(entry_param1.get())
        altura = float(entry_param2.get())
        figura = TrianguloRectangulo(base, altura)
        area = figura.calcular_area()
        perimetro = figura.calcular_perimetro()
        tipo_triangulo = figura.determinar_tipo_triangulo()
        resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nTipo: {tipo_triangulo}"

    label_resultado.config(text=resultado)

def actualizar_parametros(event):
    tipo_figura = combo_tipo_figura.get()
    if tipo_figura == "Círculo":
        label_param1.config(text="Radio:")
        label_param2.grid_remove()
        entry_param2.grid_remove()
    elif tipo_figura == "Rectángulo":
        label_param1.config(text="Base:")
        label_param2.config(text="Altura:")
        label_param2.grid()
        entry_param2.grid()
    elif tipo_figura == "Cuadrado":
        label_param1.config(text="Lado:")
        label_param2.grid_remove()
        entry_param2.grid_remove()
    elif tipo_figura == "Triángulo Rectángulo":
        label_param1.config(text="Base:")
        label_param2.config(text="Altura:")
        label_param2.grid()
        entry_param2.grid()

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")

# Creación de los widgets
label_tipo_figura = ttk.Label(root, text="Seleccione la figura:")
label_tipo_figura.grid(row=0, column=0, padx=10, pady=5, sticky="w")

combo_tipo_figura = ttk.Combobox(root, values=["Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo"])
combo_tipo_figura.grid(row=0, column=1, padx=10, pady=5)
combo_tipo_figura.bind("<<ComboboxSelected>>", actualizar_parametros)

label_param1 = ttk.Label(root, text="Parámetro 1:")
label_param1.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_param1 = ttk.Entry(root)
entry_param1.grid(row=1, column=1, padx=10, pady=5)

label_param2 = ttk.Label(root, text="Parámetro 2:")
label_param2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_param2 = ttk.Entry(root)
entry_param2.grid(row=2, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=3, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=4, columnspan=2, padx=10, pady=10)

# Inicio del bucle principal de Tkinter
root.mainloop()
