from pymongo import MongoClient

class seriesRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.client.sales_management
        self.collection = self.db.series

    def add_serie(self, name, pixels, date_added):
        product = {
            "name": name,
            "pixels": pixels,
            "date_added": date_added
        }
        result = self.collection.insert_one(product)

    def serie_exists(self, name):
        return self.collection.find_one({"name": name}) is not None

    def get_series(self):
        products = self.collection.find()
        product_list = [
            {
                "name": product.get("name", ""),
                "pixels": product.get("pixels", "Desconhecido"),
                "date_added": product.get("date_added", "")
            }
            for product in products
        ]
        return product_list

    def delete_serie(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def __del__(self):
        self.client.close()
