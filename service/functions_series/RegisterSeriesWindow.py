import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from repository.seriesRepository import seriesRepository

class RegisterSeriesWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Cadastrar Serie", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.nome_serie_label = tk.Label(self.root, text="Nome da Serie:")
        self.nome_serie_label.pack(pady=5)
        self.nome_filme_entry = tk.Text(self.root, height=1, width=60)
        self.nome_filme_entry.pack(pady=5)
        self.nome_filme_entry.bind('<KeyRelease>', self.check_duplicate)

        self.pixels_value_label = tk.Label(self.root, text="Qualidade em pixels:")
        self.pixels_value_label.pack(pady=5)
        self.pixels_value_entry = ttk.Combobox(self.root,
                                                  values=["360", "720", "1080", "Cinema"])
        self.pixels_value_entry.pack(pady=5)

        self.date_added_label = tk.Label(self.root, text="Data de Cadastro:")
        self.date_added_label.pack(pady=5)
        self.date_added_value = tk.Label(self.root, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.date_added_value.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.add_serie)
        self.register_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Voltar", command=self.callback)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_duplicate(self, event):
        db = seriesRepository()
        nome_filme = self.nome_filme_entry.get("1.0", tk.END).strip()
        if db.series_exists(nome_filme):
            self.nome_filme_entry.tag_add("duplicate", "1.0", tk.END)
            self.nome_filme_entry.tag_config("duplicate", foreground="red")
        else:
            self.nome_filme_entry.tag_remove("duplicate", "1.0", tk.END)

    def add_serie(self):
        nome_filme = self.nome_filme_entry.get("1.0", tk.END).strip().split('*', 1)[0].strip()
        pixels = self.pixels_value_entry.get()
        date_added = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtendo a data e hora atual

        if nome_filme and pixels:
            db = seriesRepository()
            if db.series_exists(nome_filme):
                messagebox.showwarning("Erro", f"Produto com o nome '{nome_filme}' já existe.")
            else:
                print(f"Cadastrando produto: Nome={nome_filme}, Pixels={pixels}, Data de Cadastro={date_added}")  # Depuração
                db.add_serie(nome_filme, pixels, date_added)
                messagebox.showinfo("Sucesso", "Serie cadastrada com sucesso!")
                self.nome_filme_entry.delete("1.0", tk.END)
                self.pixels_value_entry.set('')
                self.nome_filme_entry.tag_remove("duplicate", "1.0", tk.END)  # Resetar a cor do texto
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Código de exemplo para iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterSeriesWindow(root, callback=lambda: print("Voltar para o menu principal"))
    root.mainloop()
