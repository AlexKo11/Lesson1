price=100
discount=5
price_with_discount=price-price*discount/100
print(price_with_discount)


def discounted(price, discount)
    price=abs(float(price))
    discount=abs(float(discount))
    if discount>=100:
        price_with_discount=price
    else:
        price_with_discount=price-(price*discount/100)
    print(price_with_discount)