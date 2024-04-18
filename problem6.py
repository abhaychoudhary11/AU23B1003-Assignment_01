##5
x = int(input("Annual Site Profit: "))
y = int(input("Current Conversion Rate: "))
z = int(input("Improved Conversion Rate: "))
a = int(input("Improvement Cost: "))
b = int(input("Expected Project Life: "))
def fgp(x,y,z,a,b):
    f = (x * (z / y) - x) * (((1 + 0.05) ** 3) - 1) / 0.05 - a * ((1 + 0.05) ** 3)
    return f
def tgfi(f):
    t = (f / ((1+0.05) ** 3))
    return t
def agfi(t, b):
    ag = (t / b)
    return ag
def aroi(ag, a):
    ar = (ag / a)
    return ar
def troi(t, a):
    Tr = (t / a)
    return Tr
f = fgp(x, y, z, a, b)
t = tgfi(f)
ag = agfi(t, b)
ar = aroi(ag, a)
Tr = troi(t, a)
print("Future Gain Profit: ", int(f))
print("Total Gain from Improvement:",int(t))
print("Annual Gain from Improvement:",int(ag))
print("Annual ROI:",int(ar),":1")
print("Total ROI:",int(Tr),":1")
