price = 1000
tax = 1.1

def add_goods_total(price: int, tax: float) -> int:
    return price * tax

total = add_goods_total(price, tax)
print(total)