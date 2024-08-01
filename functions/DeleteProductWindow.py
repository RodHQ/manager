import tkinter as tk
from tkinter import messagebox
from database import Database

class DeleteProductWindow:
    def __init__(self, root, callback, product_name):
        self.root = root
        self.callback = callback
        self.product_name = product_name

        self.root.geometry("400x300")  # Definindo o tamanho da janela de exclusão
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Atenção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.texto_1_label = tk.Label(self.root, text="Você está prestes a deletar o produto:")
        self.texto_1_label.pack(pady=10)
        self.texto_2_label = tk.Label(self.root, text=self.product_name)
        self.texto_2_label.pack(pady=10)
        self.texto_3_label = tk.Label(self.root, text="deseja prosseguir?", font="bold")
        self.texto_3_label.pack(pady=10)

    #    self.product_name_entry = tk.Entry(self.root)
        #   self.product_name_entry.pack(pady=5)
        #       self.product_name_entry.insert(0, self.product_name)
        #      self.product_name_entry.config(state='disabled')

        self.delete_button = tk.Button(self.root, text="Deletar", command=self.remove_product)
        self.delete_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Voltar", command=self.close_window)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def remove_product(self):
        db = Database()
        if db.delete_product(self.product_name):
            self.callback()
            self.root.destroy()
        else:
            messagebox.showwarning("Erro", "Produto não encontrado.")

    def close_window(self):
        self.root.destroy()
        self.callback()
