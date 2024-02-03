price = 1000

def add_goods_total(price, tax) -> int:
    tax = price * 0.1
    return price + tax
    
total = add_goods_total(price, 10)
print(total)