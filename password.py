
import random as r


# # This code generates a random password based on specified criteria.
# l= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# n=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# s=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", ',', '.', '<', '>', '/', '?', '`', '~']

# # length = input("Enter desired password length (8-16): ")
# def gen_password(length=8):
#     if length < 8 or length > 16:
#         raise ValueError("Password length must be between 8 and 16")
    
#     char_pool = l + n + s #combine all the data which made the  secure password   
#     letter = r.choice(l)
#     number = r.choice(n)
#     special_char = r.choice(s)

#     password_chars = [letter, number, special_char]

#     remaining_length =length- len(password_chars)
#     password_chars += r.choices(char_pool, k=remaining_length)

#     r.shuffle(password_chars)

#     password = ''.join(str(c) for c in password_chars)

#     return password


# def main():
#     while True:
#         try:
#             length_input = input("Enter desired password length (8-16): ").strip()
#             length = int(length_input)
#             if 8 <= length <= 16:
#                 break
#             else:
#                 print("Please enter a number between 8 and 16.")
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")
#     generated_password = gen_password(length=length)
#     print("\nGenerated Password:\n" , generated_password)



# if __name__ == "__main__":
#     main()



   
   
   
# # while len(password_chars) < length:
#         # password_chars.append(r.choice(char_pool))



# # def generate_password(length=8, use_uppercase=True, use_numbers=True, use_special_chars=True):
# #     characters = l.copy()
    
# #     if use_uppercase:
# #         characters += [char.upper() for char in l]
# #     if use_numbers:
# #         characters += n
# #     if use_special_chars:
# #         characters += s
    
# #     password = ''.join(r.choices(characters, k=length))
# #     return password



import string as s
import random as r

# Character lists
lowercase_letters = list(s.ascii_lowercase)
uppercase_letters = list(s.ascii_uppercase)
numbers = list(map(str, range(10)))  # Convert numbers to strings
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", ',', '.', '<', '>', '/', '?', '`', '~']

def get_password_length():
    """Prompt the user for a password length between 8 and 16."""
    while True:
        try:
            length_input = input("Enter desired password length (8-16): ").strip()
            length = int(length_input)
            if 8 <= length <= 16:
                return length
            else:
                print("Please enter a number between 8 and 16.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def generate_password(length):
    """Generate a random password of the specified length."""
    if length < 8 or length > 16:
        raise ValueError("Password length must be between 8 and 16")

    # Ensure at least one character from each category
    password_chars = [
        r.choice(lowercase_letters),
        r.choice(uppercase_letters),
        r.choice(numbers),
        r.choice(special_characters)
    ]

    # Fill  the password length with random choices from all character 
    char_pool = lowercase_letters + uppercase_letters + numbers + special_characters
    remaining_length = length - len(password_chars)
    password_chars += r.choices(char_pool, k=remaining_length)

    # Shuffle the characters to ensure randomness
    r.shuffle(password_chars)

    # Join the characters to form the final password string
    return ''.join(password_chars)

def main():
    length = get_password_length()
    generated_password = generate_password(length)
    print("\nGenerated Password:\n", generated_password)

if __name__ == "__main__":
    main()
