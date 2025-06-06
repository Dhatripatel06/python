# user define function
def rectangle_area(length, width):  # with perameater 
    area = length * width
    return area  # with return statement
    print("area is ...=",area)

length = int(input("Enter length rectangle  "))
width = int(input("Enter width rectangle  "))

ans = rectangle_area( length ,width)
print("area is = ",ans)


