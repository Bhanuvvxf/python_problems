#Apply Discount (using map and a lambda)

prices = [100.0,150.0,500.0,600.0]
discount_prices = map(lambda x :x - (x * 0.1 ), prices)
print(list(discount_prices))