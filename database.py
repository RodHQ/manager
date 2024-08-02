from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.client.sales_management
        self.collection = self.db.filmes  # Alterado para a coleção 'filmes'

    def add_product(self, name, genre, year, pixels, date_added):
        product = {
            "name": name,
            "genre": genre,
            "year": year,
            "pixels": pixels,
            "date_added": date_added
        }
        result = self.collection.insert_one(product)
        print(f"Produto adicionado: {result.inserted_id}")  # Depuração: imprimir o ID do produto adicionado

    def product_exists(self, name):
        return self.collection.find_one({"name": name}) is not None

    def get_products(self):
        products = self.collection.find()
        product_list = [
            {
                "name": product.get("name", ""),
                "genre": product.get("genre", "Desconhecido"),
                "year": product.get("year", "Desconhecido"),
                "pixels": product.get("pixels", "Desconhecido"),
                "date_added": product.get("date_added", "")
            }
            for product in products
        ]
        print(product_list)  # Depuração: imprimir a lista de produtos
        return product_list

    def delete_product(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def __del__(self):
        self.client.close()
