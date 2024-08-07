import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from repository.documentariosRepository import documentariosRepository


class RegisterDocumentariosWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Cadastrar Documentario", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.nome_documentario_label = tk.Label(self.root, text="Nome do Documentario:")
        self.nome_documentario_label.pack(pady=5)
        self.nome_filme_entry = tk.Text(self.root, height=1, width=60)
        self.nome_filme_entry.pack(pady=5)
        self.nome_filme_entry.bind('<KeyRelease>', self.check_duplicate)

        self.genero_value_label = tk.Label(self.root, text="Gênero:")
        self.genero_value_label.pack(pady=5)
        self.genero_value_combobox = ttk.Combobox(self.root,
                                                  values=["Ação", "Comédia", "Drama", "Fantasia", "Terror", "Romance",
                                                          "Ficção", "Ficção Cientifica", "Guerra", "Desenho", "Disney",
                                                          "Heróis", "Suspense", "Aventura", "Comédia Romantica"])
        self.genero_value_combobox.pack(pady=5)

        self.ano_value_label = tk.Label(self.root, text="Ano de criação:")
        self.ano_value_label.pack(pady=5)
        self.ano_value_entry = tk.Entry(self.root)
        self.ano_value_entry.pack(pady=5)

        self.pixels_value_label = tk.Label(self.root, text="Qualidade em pixels:")
        self.pixels_value_label.pack(pady=5)
        self.pixels_value_entry = ttk.Combobox(self.root,
                                               values=["360", "720", "1080", "Cinema"])
        self.pixels_value_entry.pack(pady=5)

        self.date_added_label = tk.Label(self.root, text="Data de Cadastro:")
        self.date_added_label.pack(pady=5)
        self.date_added_value = tk.Label(self.root, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.date_added_value.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.add_documentario)
        self.register_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Voltar", command=self.callback)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_duplicate(self, event):
        db = documentariosRepository()
        nome_filme = self.nome_filme_entry.get("1.0", tk.END).strip()
        if db.documentario_exists(nome_filme):
            self.nome_filme_entry.tag_add("duplicate", "1.0", tk.END)
            self.nome_filme_entry.tag_config("duplicate", foreground="red")
        else:
            self.nome_filme_entry.tag_remove("duplicate", "1.0", tk.END)

    def add_documentario(self):
        nome_filme = self.nome_filme_entry.get("1.0", tk.END).strip().split('*', 1)[0].strip()
        genero = self.genero_value_combobox.get()
        ano = self.ano_value_entry.get()
        pixels = self.pixels_value_entry.get()
        date_added = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtendo a data e hora atual

        if nome_filme and genero and ano and pixels:
            db = documentariosRepository()
            if db.documentario_exists(nome_filme):
                messagebox.showwarning("Erro", f"Produto com o nome '{nome_filme}' já existe.")
            else:
                print(
                    f"Cadastrando produto: Nome={nome_filme}, Gênero={genero}, Ano={ano}, Pixels={pixels}, Data de Cadastro={date_added}")  # Depuração
                db.add_documentario(nome_filme, genero, ano, pixels, date_added)
                messagebox.showinfo("Sucesso", "Documentario cadastrado com sucesso!")
                self.nome_filme_entry.delete("1.0", tk.END)
                self.genero_value_combobox.set('')
                self.ano_value_entry.delete(0, tk.END)
                self.pixels_value_entry.set('')
                self.nome_filme_entry.tag_remove("duplicate", "1.0", tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
