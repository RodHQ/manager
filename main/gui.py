import tkinter as tk
from repository.filmesRepository import filmesRepository
from repository.seriesRepository import seriesRepository
from repository.animesRepository import animesRepository
from repository.novelasRepository import novelasRepository
from repository.documentariosRepository import documentariosRepository


class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu inicial")

        self.db_filmes = filmesRepository()
        self.db_series = seriesRepository()
        self.db_animes = animesRepository()
        self.db_novelas = novelasRepository()
        self.db_documentarios = documentariosRepository()

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        self.root.geometry("500x350")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Filmes", command=self.create_sub_menu_filmes)
        self.register_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Séries", command=self.create_sub_menu_series)
        self.register_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Animes", command=self.create_sub_menu_animes)
        self.register_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Novelas", command=self.create_sub_menu_novelas)
        self.register_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Documentarios", command=self.create_sub_menu_documentarios)
        self.register_button.pack(pady=10)

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

    def create_sub_menu_animes(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.register_animes)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_animes)
        self.query_button.pack(pady=10)

    def register_animes(self):
        from service.functions_animes.RegisterAnimesWindow import RegisterAnimesWindow
        RegisterAnimesWindow(self.root, self.create_main_menu)

    def query_animes(self):
        from service.functions_animes.QueryAnimesWindow import QueryAnimesWindow
        QueryAnimesWindow(self.root, self.create_main_menu)

    def create_sub_menu_novelas(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.register_novelas)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_novelas)
        self.query_button.pack(pady=10)

    def register_novelas(self):
        from service.functions_novelas.RegisterNovelasWindow import RegisterNovelasWindow
        RegisterNovelasWindow(self.root, self.create_main_menu)

    def query_novelas(self):
        from service.functions_novelas.QueryNovelasWindow import QueryNovelasWindow
        QueryNovelasWindow(self.root, self.create_main_menu)

    def create_sub_menu_documentarios(self):
        self.clear_window()

        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Selecione uma opção", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.register_button = tk.Button(self.root, text="Cadastrar", command=self.register_documentarios)
        self.register_button.pack(pady=10)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_documentarios)
        self.query_button.pack(pady=10)

    def register_documentarios(self):
        from service.functions_documentarios.RegisterDocumentariosWindow import RegisterDocumentariosWindow
        RegisterDocumentariosWindow(self.root, self.create_main_menu)

    def query_documentarios(self):
        from service.functions_documentarios.QueryDocumentariosWindow import QueryDocumentariosWindow
        QueryDocumentariosWindow(self.root, self.create_main_menu)
