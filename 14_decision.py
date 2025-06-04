# if statement-
r = int(input("Enter the redius"))

if r <0:
    r = -r
area = r*r*r
print("The area of the circle is", area)




#if else

age = int(input("Enter the age "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")



# elif 
grade = int(input("Enter the grade "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Below C")



#   neasted if
username = input("Enter username")
password = (input("Enter the password"))
otp = (input("Enter the otp"))

if username == "admin":
    if password == "secret123":
        if otp == "123456":
            print("Access granted to admin dashboard")
        else:
            print("Valid username and password, but wrong OTP")
    else:
        print("Valid username, but wrong password")
else:
    print("Invalid username")