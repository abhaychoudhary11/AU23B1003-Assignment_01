x = int(input("Annual Site Profit: "))
y = int(input("Current Conversion Rate: "))
z = int(input("Improved Conversion Rate: "))
a = int(input("Improvement Cost: "))
b = int(input("Expected Project Life: "))
f = (x * (z / y) - x) * (((1 + 0.05) ** 3) - 1) / 0.05 - a * ((1 + 0.05) ** 3)
print("Future Gain Profit: ", int(f))
t = (f / ((1+0.05) ** 3))
print("Total Gain from Improvement:",int(t))
ag = (t / b)
print("Annual Gain from Improvement:",int(ag))
ar = (ag / a)
print("Annual ROI:",int(ar))
Tr = (t / a)
print("Total ROI:",int(Tr))
