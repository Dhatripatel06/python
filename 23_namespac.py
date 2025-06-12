# Global variable
shape = "rectangle"

def calculate_area():
    # Local variable with same name
    shape = "square"
    side = int(input("enter the number"))
    area = side * side
    print("shape",shape ,"area",area)

# Call the function
calculate_area()

# Outside the function
print(shape)
# the reson of print this to define that its a globle variable

