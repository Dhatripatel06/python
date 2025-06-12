import modifymath
# Call function
n= int(input("Enter the number "))
circle = modifymath.area_circle(n)
print('circle area = ',circle)

rectangle = modifymath.area_rectangle(n,n)
print("rectangle area = ",rectangle)

triangle = modifymath.area_triangle(n,n)
print("triangle area = ",triangle)

