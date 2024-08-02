import tkinter as tk
from datetime import datetime
from tkinter import simpledialog, messagebox
from database import Database

class RegisterProductWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.root.geometry("500x600")  # Definindo o tamanho da janela de cadastro
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Cadastrar Filme", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.nome_filme_label = tk.Label(self.root, text="Nome do Filme:")
        self.nome_filme_label.pack(pady=5)
        self.nome_filme_entry = tk.Entry(self.root)
        self.nome_filme_entry.pack(pady=5)

        self.genero_value_label = tk.Label(self.root, text="Gênero:")
        self.genero_value_label.pack(pady=5)
        self.genero_value_entry = tk.Entry(self.root)
        self.genero_value_entry.pack(pady=5)

        self.ano_value_label = tk.Label(self.root, text="Ano de criação:")
        self.ano_value_label.pack(pady=5)
        self.ano_value_entry = tk.Entry(self.root)
        self.ano_value_entry.pack(pady=5)

        self.pixels_value_label = tk.Label(self.root, text="Qualidade em pixels:")
        self.pixels_value_label.pack(pady=5)
        self.pixels_value_entry = tk.Entry(self.root)
        self.pixels_value_entry.pack(pady=5)

        self.date_added_label = tk.Label(self.root, text="Data de Cadastro:")
        self.date_added_label.pack(pady=5)
        self.date_added_value = tk.Label(self.root, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.date_added_value.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.add_product)
        self.register_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Voltar", command=self.callback)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_product(self):
        nome_filme = self.nome_filme_entry.get()
        genero = self.genero_value_entry.get()
        ano = self.ano_value_entry.get()
        pixels = self.pixels_value_entry.get()
        date_added = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtendo a data e hora atual

        if nome_filme and genero and ano and pixels:
            db = Database()
            print(f"Cadastrando produto: Nome={nome_filme}, Gênero={genero}, Ano={ano}, Pixels={pixels}, Data de Cadastro={date_added}")  # Depuração
            db.add_product(nome_filme, genero, ano, pixels, date_added)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.nome_filme_entry.delete(0, tk.END)
            self.genero_value_entry.delete(0, tk.END)
            self.ano_value_entry.delete(0, tk.END)
            self.pixels_value_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
