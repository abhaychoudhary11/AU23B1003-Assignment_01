name=input("name:")
brand=input("brand name:")
size=input("size:")
def get_tshirt(brand, size):
    available_brand = ["gucci","armani","peter england","nike"]
    available_size = {"gucci":["S"],"armani":["M"],"peter england":["XL"],"nike":["S","M","L","XL"]}
    if brand in available_brand:
        if size in available_size[brand]:
            return "hi",name,"the brand you are looking for is available in our store and size is also available"
        else:
            return "hi",name,"the brand you are looking for is available in our store but the size you asked for is not available"
    else:
        return "hi",name,"Unfortunately the brand you are looking for is not available in our store"
print(get_tshirt(brand, size))
