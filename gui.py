import tkinter as tk
from database import Database
from functions.QueryProductWindow import QueryProductWindow
from functions.RegisterProductWindow import RegisterProductWindow


class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu inicial")

        self.db = Database()

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        self.root.geometry("400x300")  # Definindo o tamanho da janela principal

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar Produto", command=self.register_product)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar Produto", command=self.query_product)
        self.query_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_product(self):
        RegisterProductWindow(self.root, self.create_main_menu)

    def query_product(self):
        QueryProductWindow(self.root, self.create_main_menu)


