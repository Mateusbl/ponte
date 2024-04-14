import tkinter as tk
from tkinter import ttk
from decimal import Decimal
from math import sqrt

class Fio:
    def __init__(self, comprimento=0, peso=0):
        self.comprimento = comprimento
        self.peso = peso

class Barra:
    def __init__(self):
        self.comprimento = 0
        self.n_fios = 0
        self.peso = 0
        self.nome = ""
        self.esforco_interno = 0
        self.tipo_de_esforco = ""

    def calcular_fio(self):
        if self.tipo_de_esforco == 'C':
            resultadoc = sqrt((self.esforco_interno * self.comprimento**2) / (27906 * 1**4))
            self.n_fios = resultadoc
        elif self.tipo_de_esforco == 'T':
            resultadot = self.esforco_interno / Decimal(42.67)
            self.n_fios = resultadot
        else:
            print('tipo invalido')

class Ponte:
    def __init__(self):
        self.peso = 0
        self.capacidade = 0
        self.n_barras = 0
        self.geometria = ""
        self.descricao_teste = ""
        self.n_teste = 0

def calculate():
    try:
        ponte = Ponte()
        ponte.peso = Decimal(peso_entry.get())
        ponte.capacidade = int(capacidade_entry.get())
        ponte.n_barras = int(n_barras_entry.get())
        ponte.geometria = geometria_entry.get()
        ponte.descricao_teste = descricao_teste_entry.get()
        ponte.n_teste = int(n_teste_entry.get())

        if ponte.peso >= 1000:
            result_label.config(text='Ponte inválida')
        else:
            result_label.config(text='Ponte criada com sucesso')
    except ValueError:
        result_label.config(text="Por favor, insira valores válidos.")

# Create the main application window
root = tk.Tk()
root.title("Criador de Pontes")

# Create input fields
peso_label = ttk.Label(root, text="Peso da Ponte:")
peso_label.grid(row=0, column=0, padx=5, pady=5)
peso_entry = ttk.Entry(root)
peso_entry.grid(row=0, column=1, padx=5, pady=5)

capacidade_label = ttk.Label(root, text="Capacidade da Ponte (gramas):")
capacidade_label.grid(row=1, column=0, padx=5, pady=5)
capacidade_entry = ttk.Entry(root)
capacidade_entry.grid(row=1, column=1, padx=5, pady=5)

n_barras_label = ttk.Label(root, text="Número de Barras:")
n_barras_label.grid(row=2, column=0, padx=5, pady=5)
n_barras_entry = ttk.Entry(root)
n_barras_entry.grid(row=2, column=1, padx=5, pady=5)

geometria_label = ttk.Label(root, text="Geometria da Ponte:")
geometria_label.grid(row=3, column=0, padx=5, pady=5)
geometria_entry = ttk.Entry(root)
geometria_entry.grid(row=3, column=1, padx=5, pady=5)

descricao_teste_label = ttk.Label(root, text="Descrição do Teste:")
descricao_teste_label.grid(row=4, column=0, padx=5, pady=5)
descricao_teste_entry = ttk.Entry(root)
descricao_teste_entry.grid(row=4, column=1, padx=5, pady=5)

n_teste_label = ttk.Label(root, text="Número do Teste:")
n_teste_label.grid(row=5, column=0, padx=5, pady=5)
n_teste_entry = ttk.Entry(root)
n_teste_entry.grid(row=5, column=1, padx=5, pady=5)

# Create a button to trigger the calculation
calculate_button = ttk.Button(root, text="Criar Ponte", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create a label to display the results
result_label = ttk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()