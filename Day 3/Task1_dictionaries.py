product={
    "Pen":20,
    "BOOK":150,
    "Bag":1000,
    "Bottel":500,
    "Pencil":10
}
above_100={product:price for product,price in product.items()if price>100}

print("Productnpriced above 100:")
print(above_100)