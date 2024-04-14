import tkinter as tk
from tkinter import ttk
from decimal import Decimal
from math import sqrt


def calculate():
    try:
        esforco_interno = Decimal(esforco_interno_entry.get())
        tipo = tipo_combobox.get()
        comprimento = Decimal(comprimento_entry.get())

        if tipo == "Compressão (C)":
            resultadoc = sqrt((esforco_interno * comprimento ** 2) / (27906 * 1 ** 4))
            result_label.config(text=f"O número de fios necessários é: {resultadoc}")
        elif tipo == "Tração (T)":
            resultadot = esforco_interno / Decimal(42.67)
            result_label.config(text=f"O número de fios necessários é: {resultadot}")
        else:
            result_label.config(text="Tipo inválido")
    except ValueError:
        result_label.config(text="Por favor, insira valores válidos.")


# Create the main application window
root = tk.Tk()
root.title("Calculadora de Esforço Interno")

# Create input fields
esforco_interno_label = ttk.Label(root, text="Esforço Interno (N):")
esforco_interno_label.grid(row=0, column=0, padx=5, pady=5)
esforco_interno_entry = ttk.Entry(root)
esforco_interno_entry.grid(row=0, column=1, padx=5, pady=5)

tipo_label = ttk.Label(root, text="Tipo de Esforço:")
tipo_label.grid(row=1, column=0, padx=5, pady=5)
tipo_combobox = ttk.Combobox(root, values=["Compressão (C)", "Tração (T)"])
tipo_combobox.grid(row=1, column=1, padx=5, pady=5)
tipo_combobox.current(0)

comprimento_label = ttk.Label(root, text="Comprimento da Peça (mm):")
comprimento_label.grid(row=2, column=0, padx=5, pady=5)
comprimento_entry = ttk.Entry(root)
comprimento_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a button to trigger the calculation
calculate_button = ttk.Button(root, text="Calcular", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create a label to display the results
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()