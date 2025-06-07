
# function have two typers UDF and buit in

# buit in function
list = [1, 2, 3, 4, 5]
length = len(list)
print("Length of the list:", length)
   
# user define function
# def rectangle_area(length, width):  # with perameater 
#     area = length * width
#     return area  # with return statement
#     print("area is ...=",area)


# length = int(input("Enter length rectangle  "))
# width = int(input("Enter width rectangle  "))

# ans = rectangle_area( length ,width)
# print("area is = ",ans)

# with argument and with returns a value.
def square(x):
       return x ** 2

result = square(5)
print("Square of 5:", result)
   
#  more then two arguments with return
def multiply(a, b):
       return a * b

result = multiply(4, 3)
print("Product of 4 and 3:", result)

# without argument with return

def get_pi():
       return 3.14159

result = get_pi()
print("Value of Pi:", result)

#with argument without return

def append_to_list(my_list, item):
       my_list.append(item)
       print("Updated list:", my_list)

my_list = [1, 2, 3]
append_to_list(my_list, 4)

#without argument and no return

def display_menu():
       print("1. Option 1")
       print("2. Option 2")
       print("3. Exit")

display_menu()

   
   



