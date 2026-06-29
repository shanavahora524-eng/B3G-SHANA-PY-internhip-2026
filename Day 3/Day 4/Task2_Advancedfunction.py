def apply_discount(price,percent=10):
    discount=price*percent/100
    final_price=price-discount

print("Price After Default Discount:",apply_discount(4500))
print("Price After 20% Discount:",apply_discount(6500,percent=20))