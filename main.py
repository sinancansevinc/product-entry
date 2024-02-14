import xml.etree.ElementTree as ET

from DatabaseManager import DatabaseManager
from Product import Product
from RegexParser import RegexParser


def get_products(database):
    products = database.fetch_all()

    if len(list(products)) == 0:
        print("No products found")
        return

    for product in list(products):
        print("----------------------------")
        print(product)
        print("----------------------------")


def delete_products(database):
    database.delete_all()
    print("All products deleted")
    return True


def parse_xml_add_products(database):
    tree = ET.parse('products.xml')
    product_roots = tree.getroot()
    products_to_db = []

    for product_child in product_roots:
        product_id = product_child.attrib['ProductId']
        product_name = product_child.attrib['Name'].capitalize()
        images = [image.attrib["Path"]
                  for image in product_child.find(".//Images").findall("Image")]

        product_details = {detail.attrib["Name"]: detail.attrib["Value"] for detail in product_child.find(
            ".//ProductDetails").findall("ProductDetail")}

        description = product_child.find(".//Description").text

        fabric_info, product_measurements, model_info, size_info = RegexParser.parse_description(
            description)

        product = Product(product_name, product_id, product_details["Color"], (product_details["Price"]),
                          RegexParser.parse_price(product_details["DiscountedPrice"]), images, product_details["ProductType"], int(product_details[
                              "Quantity"]), size_info, product_details["Series"], fabric_info, model_info, product_measurements
                          )
        products_to_db.append(product)

    database.create_range(products_to_db)


if __name__ == "__main__":
    database = DatabaseManager()

    while True:
        print("1. Get all products")
        print("2. Parse xml and add products")
        print("3. Delete all products")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_products(database)
            continue

        elif choice == "2":
            parse_xml_add_products(database)
            continue

        elif choice == "3":
            delete_products(database)
            continue

        elif choice == "4":
            break

        else:
            print("Invalid choice")
            continue
        break
