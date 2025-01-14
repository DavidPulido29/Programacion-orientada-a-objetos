import tkinter as tk
from tkinter import ttk

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = float(patrimonio)
        self.estrato_social = int(estrato_social)

    def calcular_pago_matricula(self):
        pago_base = 50000
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            aumento = self.patrimonio * 0.03
            return pago_base + aumento
        else:
            return pago_base

    def mostrar_informacion(self):
        pago_matricula = self.calcular_pago_matricula()
        return self.numero_inscripcion, self.nombres, pago_matricula

# Función para manejar la lógica de cálculo
def calcular():
    try:
        numero_inscripcion = entry_numero_inscripcion.get()
        nombres = entry_nombres.get()
        patrimonio = entry_patrimonio.get()
        estrato_social = entry_estrato_social.get()
        
        # Verificación de entradas vacías
        if not numero_inscripcion or not nombres or not patrimonio or not estrato_social:
            label_resultado.config(text="Por favor, ingresa todos los campos.")
            return
        
        estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato_social)
        info = estudiante.mostrar_informacion()

        label_resultado.config(text=f"Número de inscripción: {info[0]}\n"
                                   f"Nombres: {info[1]}\n"
                                   f"Pago de matrícula: ${info[2]:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa valores válidos.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Calculadora de Matrícula")

# Creación de los widgets
label_numero_inscripcion = ttk.Label(root, text="Número de inscripción:")
label_numero_inscripcion.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_numero_inscripcion = ttk.Entry(root)
entry_numero_inscripcion.grid(row=0, column=1, padx=10, pady=5)

label_nombres = ttk.Label(root, text="Nombres del estudiante:")
label_nombres.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_nombres = ttk.Entry(root)
entry_nombres.grid(row=1, column=1, padx=10, pady=5)

label_patrimonio = ttk.Label(root, text="Patrimonio del estudiante:")
label_patrimonio.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_patrimonio = ttk.Entry(root)
entry_patrimonio.grid(row=2, column=1, padx=10, pady=5)

label_estrato_social = ttk.Label(root, text="Estrato social del estudiante:")
label_estrato_social.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_estrato_social = ttk.Entry(root)
entry_estrato_social.grid(row=3, column=1, padx=10, pady=5)

button_calcular = ttk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=4, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=5, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
