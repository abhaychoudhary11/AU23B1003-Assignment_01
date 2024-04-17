def restaurent(order):
    orders = ["french fries", "Pani puri", "burger"]
    for i in range(len(orders)):
        print("preparing your order:",orders[i])
    print("the following orders have been dispatched:")
    for order in orders:
        print(order)
restaurent(order)
