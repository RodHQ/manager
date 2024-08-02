import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from functions.DeleteProductWindow import DeleteProductWindow

class QueryProductWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.root.geometry("1000x500")  # Definindo o tamanho da janela de consulta
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Consulta de Produtos", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Frame para a barra de pesquisa
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(fill=tk.X, padx=20, pady=10, anchor='e')

        self.search_label = tk.Label(self.search_frame, text="Pesquisar:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', self.filter_products)

        self.tree = ttk.Treeview(self.root, columns=("name", "genre", "year", "pixels", "date_added"), show='headings')
        self.tree.heading("name", text="Nome do Filme")
        self.tree.heading("genre", text="Gênero")
        self.tree.heading("year", text="Ano de Criação")
        self.tree.heading("pixels", text="Qualidade em Pixels")
        self.tree.heading("date_added", text="Data de Cadastro")

        self.tree.column("name", width=200, anchor=tk.CENTER)
        self.tree.column("genre", width=150, anchor=tk.CENTER)
        self.tree.column("year", width=100, anchor=tk.CENTER)
        self.tree.column("pixels", width=150, anchor=tk.CENTER)
        self.tree.column("date_added", width=200, anchor=tk.CENTER)

        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)

        self.load_products()

        self.delete_button = tk.Button(self.root, text="Deletar Produto", command=self.delete_product)
        self.delete_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Voltar", command=self.callback)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def load_products(self):
        db = Database()
        self.products = db.get_products()
        self.display_products(self.products)

    def display_products(self, products):
        self.clear_treeview()
        for product in products:
            self.tree.insert("", tk.END, values=(product['name'], product['genre'], product['year'], product['pixels']+"p", product['date_added']))

    def filter_products(self, event):
        query = self.search_entry.get().lower()
        filtered_products = [
            product for product in self.products
            if query in product['name'].lower() or query in product['genre'].lower()
        ]
        self.display_products(filtered_products)

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            product_name = item['values'][0]
            self.show_delete_product_window(product_name)
        else:
            messagebox.showwarning("Aviso", "Selecione um produto para deletar.")

    def show_delete_product_window(self, product_name):
        delete_window = tk.Toplevel(self.root)
        DeleteProductWindow(delete_window, self.load_products, product_name)

# Função de teste
def test():
    root = tk.Tk()
    def go_back():
        print("Voltar")
    app = QueryProductWindow(root, go_back)
    root.mainloop()

# Descomente a linha abaixo para testar a interface
# test()
