import tkinter as tk
from tkinter import ttk

class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = float(salario_hora)
        self.horas_trabajadas = int(horas_trabajadas)

    def calcular_salario_mensual(self):
        salario_mensual = self.salario_hora * self.horas_trabajadas
        return salario_mensual

    def mostrar_resultado(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            return f"Nombre del empleado: {self.nombre}\nSalario mensual: ${salario_mensual:.2f}"
        else:
            return f"Nombre del empleado: {self.nombre}"

# Función para manejar la lógica de cálculo
def calcular():
    nombre = entry_nombre.get()
    salario_hora = entry_salario_hora.get()
    horas_trabajadas = entry_horas_trabajadas.get()

    # Validación de entradas
    if not nombre or not salario_hora or not horas_trabajadas:
        label_resultado.config(text="Por favor, ingresa todos los campos.")
        return

    try:
        empleado = Empleado(nombre, salario_hora, horas_trabajadas)
        resultado = empleado.mostrar_resultado()
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, ingresa valores válidos.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Salario")

# Creación de los widgets
label_nombre = ttk.Label(root, text="Nombre del empleado:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_nombre = ttk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_salario_hora = ttk.Label(root, text="Salario básico por hora:")
label_salario_hora.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_salario_hora = ttk.Entry(root)
entry_salario_hora.grid(row=1, column=1, padx=10, pady=5)

label_horas_trabajadas = ttk.Label(root, text="Horas trabajadas en el mes:")
label_horas_trabajadas.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_horas_trabajadas = ttk.Entry(root)
entry_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=3, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=4, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
