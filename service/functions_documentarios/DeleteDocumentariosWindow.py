import tkinter as tk
from tkinter import messagebox
from repository.documentariosRepository import documentariosRepository

class DeleteDocumentariosWindow:
    def __init__(self, root, callback, product_name):
        self.root = root
        self.callback = callback
        self.product_name = product_name

        self.root.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text=f"Tem certeza que deseja deletar '{self.product_name}'?", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.delete_button = tk.Button(self.root, text="Deletar", command=self.delete_product)
        self.delete_button.pack(pady=10)

        self.cancel_button = tk.Button(self.root, text="Cancelar", command=self.root.destroy)
        self.cancel_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def delete_product(self):
        db = documentariosRepository()
        success = db.delete_documentario(self.product_name)
        if success:
            messagebox.showinfo("Sucesso", f"Documentario '{self.product_name}' deletada com sucesso.")
        else:
            messagebox.showerror("Erro", f"Falha ao deletar o produto '{self.product_name}'.")
        self.root.destroy()
        self.callback()
