# return multipal value from the function the output is in tuple format

def calc(radius):
    area = 3.14 * radius ** 2
    circle = 2 * 3.14 * radius
    diameter = 2 * radius
    
    return area, circle, diameter

a, c, d = calc(5)
print(a,d,c)   #order dose not metter