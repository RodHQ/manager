from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.client.sales_management
        self.collection = self.db.products

    def add_product(self, name, purchase_value, date_added):
        product = {"name": name, "purchase_value": purchase_value, "date_added": date_added}
        result = self.collection.insert_one(product)
        print(f"Produto adicionado: {result.inserted_id}")  # Depuração: imprimir o ID do produto adicionado

    def delete_product(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def get_products(self):
        products = self.collection.find()
        product_list = [{"name": product["name"], "purchase_value": product["purchase_value"], "date_added": product["date_added"]} for product in products]
        print(product_list)  # Depuração: imprimir a lista de produtos
        return product_list

    def __del__(self):
        self.client.close()
