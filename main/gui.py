import tkinter as tk
from repository.filmesRepository import filmesRepository
from repository.seriesRepository import seriesRepository


class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu inicial")

        self.db_filmes = filmesRepository()
        self.db_series = seriesRepository()

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Filmes", command=self.create_sub_menu_filmes)
        self.register_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Séries", command=self.create_sub_menu_series)
        self.register_button.pack(pady=10)

    #        self.register_button = tk.Button(self.root, text="Novelas", command=self.create_sub_menu_filmes)
    #        self.register_button.pack(pady=10)

    #        self.register_button = tk.Button(self.root, text="Documentarios", command=self.create_sub_menu_filmes)
    #        self.register_button.pack(pady=10)

    # Direciona ao menu de filmes
    def create_sub_menu_filmes(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.register_filmes)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_filmes)
        self.query_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_filmes(self):
        from service.functions_filmes.RegisterFilmesWindow import RegisterFilmesWindow
        RegisterFilmesWindow(self.root, self.create_main_menu)

    def query_filmes(self):
        from service.functions_filmes.QueryFilmesWindow import QueryFilmesWindow
        QueryFilmesWindow(self.root, self.create_main_menu)

    # Direciona ao menu de series
    def create_sub_menu_series(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.register_series)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_series)
        self.query_button.pack(pady=10)

    def register_series(self):
        from service.functions_series.RegisterSeriesWindow import RegisterSeriesWindow
        RegisterSeriesWindow(self.root, self.create_main_menu)

    def query_series(self):
        from service.functions_series.QuerySeriesWindow import QuerySeriesWindow
        QuerySeriesWindow(self.root, self.create_main_menu)
