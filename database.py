from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.client.sales_management
        self.collection = self.db.filmes

    def add_product(self, name, genre, year, pixels, date_added):
        product = {
            "name": name,
            "genre": genre,
            "year": year,
            "pixels": pixels,
            "date_added": date_added
        }
        result = self.collection.insert_one(product)
        print(f"Produto adicionado: {result.inserted_id}")

    def delete_product(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def get_products(self):
        products = self.collection.find()
        print(f"Teste: collection.find(): {products}")
        product_list = [
            {
                "name": product["name"],
                "genre": product["genre"],
                "year": product["year"],
                "pixels": product["pixels"],
                "date_added": product["date_added"]
            }
            for product in products
        ]
        print(product_list)
        return product_list

    def __del__(self):
        self.client.close()
