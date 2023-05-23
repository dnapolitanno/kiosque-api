from menu import products


def calculate_tab(tables):
    subtotal = 0.0

    for table in tables:
        product_id = table['_id']
        quant = table['amount']

        product = next((item for item in products if item['_id'] == product_id), None)

        if product:
            price = product['price']
            subtotal += price * quant

    subtotal_formatado = '${:.2f}'.format(subtotal).rstrip('0').rstrip('.')

    return {'subtotal': subtotal_formatado}
