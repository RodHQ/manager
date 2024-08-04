from pymongo import MongoClient

class documentariosRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.client.sales_management
        self.collection = self.db.documentarios

    def add_documentario(self, name, genre, year, pixels, date_added):
        product = {
            "name": name,
            "genre": genre,
            "year": year,
            "pixels": pixels,
            "date_added": date_added
        }
        result = self.collection.insert_one(product)

    def documentario_exists(self, name):
        return self.collection.find_one({"name": name}) is not None

    def get_documentarios(self):
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
        return product_list

    def delete_documentario(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def __del__(self):
        self.client.close()
