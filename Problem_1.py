name=input("name:")
brand=input("brand name:")
def get_tshirt(brand):
    available=["gucci","armani","pter england","nike"]
    if brand in available:
        return "hi",name,"the brand you are looking for is available in our store"
    else:
        return "hi" ,name, "Unfortunately the brand you are looking for is not available in our store"
print(get_tshirt(brand))
