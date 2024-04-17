x=int(input("no. of order you want:"))
orders = []
for i in range(x):
    if x>1:
        y=input("dish:")
        orders.append(y)
def restaurent(order):
    for i in range(len(orders)):
        print("preparing your order:",orders[i])
    print("the following orders have been dispatched:")
    for order in orders:
        print(order)
restaurent(order)
