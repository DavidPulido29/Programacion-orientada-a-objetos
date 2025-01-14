import tkinter as tk
from tkinter import ttk

# Clase que representa a un empleado
class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = float(horas_trabajadas)
        self.valor_hora = float(valor_hora)
        self.retencion_fuente = float(retencion_fuente)

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = (self.retencion_fuente / 100) * salario_bruto
        return salario_bruto - retencion

    def mostrar_informacion(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        return (self.codigo, self.nombres, salario_bruto, salario_neto)

# Función para calcular los salarios y mostrar la información
def calcular():
    empleado = Empleado(
        entry_codigo.get(),
        entry_nombres.get(),
        entry_horas_trabajadas.get(),
        entry_valor_hora.get(),
        entry_retencion_fuente.get()
    )
    info = empleado.mostrar_informacion()
    label_resultado.config(
        text=f"Código del empleado: {info[0]}\n"
             f"Nombres del empleado: {info[1]}\n"
             f"Salario bruto: {info[2]:.2f}\n"
             f"Salario neto: {info[3]:.2f}"
    )

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Salarios")

# Creación de los widgets
label_codigo = ttk.Label(root, text="Código del empleado:")
label_codigo.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_codigo = ttk.Entry(root)
entry_codigo.grid(row=0, column=1, padx=10, pady=5)

label_nombres = ttk.Label(root, text="Nombres del empleado:")
label_nombres.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nombres = ttk.Entry(root)
entry_nombres.grid(row=1, column=1, padx=10, pady=5)

label_horas_trabajadas = ttk.Label(root, text="Horas trabajadas al mes:")
label_horas_trabajadas.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_horas_trabajadas = ttk.Entry(root)
entry_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

label_valor_hora = ttk.Label(root, text="Valor de la hora trabajada:")
label_valor_hora.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_valor_hora = ttk.Entry(root)
entry_valor_hora.grid(row=3, column=1, padx=10, pady=5)

label_retencion_fuente = ttk.Label(root, text="Retención en la fuente (%):")
label_retencion_fuente.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_retencion_fuente = ttk.Entry(root)
entry_retencion_fuente.grid(row=4, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=5, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=6, columnspan=2, padx=10, pady=10)

# Ejecución del bucle principal de Tkinter
root.mainloop()
