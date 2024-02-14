from datetime import datetime

import pymongo

from Product import Product


class DatabaseManager:
    def __init__(self):
        client = None

        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = client["lonca"]
            self.collection = self.db["products"]
        except Exception as e:
            print(f"Error: {e}")

    def fetch_one(self, product_stock_code):
        data = self.collection.find_one({'stock_code': product_stock_code})
        return data

    def create_range(self, products: list[Product]):
        try:
            product_to_table = []
            for product in products:
                is_exist = self.fetch_one(product.stock_code)
                if is_exist is None:
                    data = {
                        'stock_code': product.stock_code,
                        'color': product.color,
                        'discounted_price': product.discounted_price,
                        'images': product.images,
                        'is_discounted': product.is_discounted,
                        'name': product.name,
                        'price': product.price,
                        'price_unit': product.price_unit,
                        'product_type': product.product_type,
                        'quantity': product.quantity,
                        'sample_size': product.sample_size,
                        'series': product.series,
                        'status': product.status,
                        'fabric': product.fabric,
                        'model_measurements': product.model_measurements,
                        'product_measurements': product.product_measurements,
                        'createdAt': datetime.now()
                    }
                    product_to_table.append(data)

            if len(product_to_table) == 0:
                print("All Products are exist")

            else:
                self.collection.insert_many(
                    product_to_table)

                stock_codes = [element["stock_code"]
                               for element in product_to_table]

                print(f"Products created with stock_codes: {stock_codes}")

        except Exception as e:
            print(f"Error while creating Products: {e}")

    def fetch_all(self):
        try:
            products = self.collection.find()
            return list(products)

        except Exception as e:
            print(f"Error while fetching Products: {e}")

    def delete_all(self):
        try:
            self.collection.delete_many({})
            return True

        except Exception as e:
            print(f"Error while deleting Products: {e}")
            return False
