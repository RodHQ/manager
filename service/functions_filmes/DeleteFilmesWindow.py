import tkinter as tk
from tkinter import messagebox
from repository.filmesRepository import filmesRepository

class DeleteFilmesWindow:
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

        self.delete_button = tk.Button(self.root, text="Deletar", command=self.delete_filme)
        self.delete_button.pack(pady=10)

        self.cancel_button = tk.Button(self.root, text="Cancelar", command=self.root.destroy)
        self.cancel_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def delete_filme(self):
        db = filmesRepository()
        success = db.delete_filme(self.product_name)
        if success:
            messagebox.showinfo("Sucesso", f"Produto '{self.product_name}' deletado com sucesso.")
        else:
            messagebox.showerror("Erro", f"Falha ao deletar o produto '{self.product_name}'.")
        self.root.destroy()
        self.callback()

# Função de teste
def test():
    root = tk.Tk()
    def refresh():
        print("Atualizando lista de produtos...")
    app = DeleteFilmesWindow(root, refresh, "Produto Teste")
    root.mainloop()

# Descomente a linha abaixo para testar a interface
# test()
