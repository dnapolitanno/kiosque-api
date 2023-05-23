from menu import products


def get_product_by_id(id):
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type):
    products_by_type = []

    for product in products:
        if product['type'] == type:
            products_by_type.append(product)

    return products_by_type


def add_product(menu, **product):
    if not menu:
        new_id = 1
    else:
        new_id = max(item.get('_id', 0) for item in menu) + 1

    product['_id'] = new_id
    menu.append(product)

    return product
