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

        self.label = tk.Label(self.root, text="Cadastrar Produto", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.product_name_label = tk.Label(self.root, text="Nome do Produto:")
        self.product_name_label.pack(pady=5)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.pack(pady=5)

        self.purchase_value_label = tk.Label(self.root, text="Valor de Compra:")
        self.purchase_value_label.pack(pady=5)
        self.purchase_value_entry = tk.Entry(self.root)
        self.purchase_value_entry.pack(pady=5)

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
        product_name = self.product_name_entry.get()
        purchase_value = self.purchase_value_entry.get()
        date_added = datetime.now().strftime("%d/%m/%y %H:%M:%S")  # Obtendo a data e hora atual

        if product_name and purchase_value:
            db = Database()
            print(f"Cadastrando produto: Nome={product_name}, Valor de Compra={purchase_value}, Data de Cadastro={date_added}")  # Depuração
            db.add_product(product_name, purchase_value, date_added)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.product_name_entry.delete(0, tk.END)
            self.purchase_value_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
