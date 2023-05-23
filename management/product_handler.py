from menu import products


def get_product_by_id(id):
    for produto in products:
        if produto['_id'] == id:
            return produto
    return {}


def get_products_by_type(type):
    products_by_type = []

    for produto in products:
        if produto['type'] == type:
            products_by_type.append(produto)

    return products_by_type
