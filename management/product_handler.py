from menu import products


def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type):
    products_by_type = []

    if not isinstance(type, str):
        raise TypeError("product type must be a str")

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


def menu_report():
    product_count = len(products)

    if product_count == 0:
        average_price = 0.0
        most_common_type = "N/A"
    else:
        total_price = sum(product['price'] for product in products)
        average_price = round(total_price / product_count, 2)

        type_counts = {}
        for product in products:
            product_type = product['type']
            type_counts[product_type] = type_counts.get(product_type, 0) + 1

        most_common_type = max(type_counts, key=type_counts.get)

    report = f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
    return report


def add_product_extra(menu, *required_keys, **new_product):
    missing_keys = set(required_keys) - set(new_product.keys())
    if missing_keys:
        missing_key = missing_keys.pop()
        raise KeyError(f"field {missing_key} is required")

    extra_keys = set(new_product.keys()) - set(required_keys)
    for key in extra_keys:
        new_product.pop(key)

    if menu:
        max_id = max(product["_id"] for product in menu)
        new_id = max_id + 1
    else:
        new_id = 1

    new_product["_id"] = new_id

    menu.append(new_product)

    return new_product
