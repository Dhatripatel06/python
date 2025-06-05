# whilw loop

s= int(input("Enter the starting number: "))
e = int(input("Enter the ending number: "))

count = s

while count <= e:
    print("Count is:", count)
    count += 1



# for loop with left side 

rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
            print(j, end=" ")
    print()



# second pyramid
# rows = 4

# for i in range(1, rows + 1):
#     #  spaces
#     for space in range(rows - i):
#         print(" ", end="")

#     # Print  from 1 to i
#     for num in range(1, i + 1):
#         print(num, end=" ")

#     # for next line
#     print()
