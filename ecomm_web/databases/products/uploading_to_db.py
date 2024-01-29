import pymongo
from json_file import loading_json_file as file
from schema import product_schema as skem


def validate_product(product):
    for key, config in skem.items():
        if config["required"] and key not in product:
            raise ValueError(f"Missing required field: {key}")

        if key == "rating" and isinstance(product[key], int):
            product[key] = float(product[key])

        if key in product and not isinstance(product[key], config["type"]):
            raise ValueError(f"Invalid data type for {key}. Expected {config['type']}, but got {type(product[key])}")

        if key not in product and "default" in config:
            product[key] = config["default"]


def upload_to_mongodb(products):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")
    database_name = "ecomm"
    db = client[database_name]
    products_collection = db["products"]

    for product in products:
        validate_product(product)
        products_collection.insert_one(product)


    client.close()


products = file('products.json')['products']
upload_to_mongodb(products)
