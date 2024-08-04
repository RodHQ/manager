import tkinter as tk
from tkinter import ttk, messagebox
from repository.animesRepository import animesRepository
from service.functions_animes.DeleteAnimesWindow import DeleteAnimesWindow

class QueryAnimesWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.root.geometry("1000x500")
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Consulta de Animes", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(fill=tk.X, padx=20, pady=10, anchor='e')

        self.search_label = tk.Label(self.search_frame, text="Pesquisar:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', self.filter_animes)

        self.tree = ttk.Treeview(self.root, columns=("name", "genre", "year", "pixels", "date_added"), show='headings')
        self.tree.heading("name", text="Nome do Anime")
        self.tree.heading("genre", text="")
        self.tree.heading("year", text="")
        self.tree.heading("pixels", text="Qualidade em Pixels")
        self.tree.heading("date_added", text="Data de Cadastro")

        self.tree.column("name", width=200, anchor=tk.CENTER)
        self.tree.column("pixels", width=150, anchor=tk.CENTER)
        self.tree.column("date_added", width=200, anchor=tk.CENTER)

        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)

        self.load_products()

        self.delete_button = tk.Button(self.root, text="Deletar Produto", command=self.delete_anime)
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
        db = animesRepository()
        self.animes = db.get_animes()
        self.display_animes(self.animes)

    def display_animes(self, products):
        self.clear_treeview()
        for product in products:
            pixels = product['pixels']
            if pixels.lower() != "cinema":
                pixels += "p"
            self.tree.insert("", tk.END,
                             values=(product['name'], pixels, product['date_added']))

    def filter_animes(self, event):
        query = self.search_entry.get().lower()
        filtered_products = [
            product for product in self.animes
            if query in product['name'].lower()
        ]
        self.display_animes(filtered_products)

    def delete_anime(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            product_name = item['values'][0]
            self.show_delete_anime_window(product_name)
        else:
            messagebox.showwarning("Aviso", "Selecione um anime para deletar.")

    def show_delete_anime_window(self, anime_name):
        delete_window = tk.Toplevel(self.root)
        DeleteAnimesWindow(delete_window, self.load_products, anime_name)
