import random as r

str = "hello "
s ="wer456"
u="DFGH"
sp= "  "
n= "456"
t="Hello World"
# n=['a','b','c','d','e','f','g','h','i','j']
# m=['1','2','3','4','5','6','7','8','9','0']

# s = "--"
# print (s.join(n))

#  str.isalnum() String consists of only alphanumeric characters (no symbols)
print("using s",s.isalnum())
print("using str ",str.isalnum())



#  str.isalpha() String consists of only alphabetic characters (no symbols)
print(" using str ",str.isalpha())
print("using str ",str.isalpha())

#  str.islower() String’s alphabetic characters are all lower case
print("using str ",str.islower())
print("using str ",str.islower())

#  str.isnumeric() String consists of only numeric characters
print("using n   ",n.isnumeric())
print("using str ",str.isnumeric())

#  str.isspace() String consists of only whitespace characters
print("using s  ",sp.isspace())
print("using str ",str.isspace())

#  str.istitle() String is in title case
print("using t   ",t.istitle())
print("using str ",str.istitle())

#  str.isupper() String’s alphabetic characters are all upper cas
print("using u   ",u.isupper())
print("using str ",str.isupper())


list = ["India","usa","UK","Canada","Australia"]
s = ","
print (s.join(list))
name = "The easylearn Academy"
print("replace",name.replace('e','E',1))
# Replace the first occurrence of 'e' with 'E' without using the built-in replace method

temp_name = name.replace('e', 'TEMP', 1).replace('e', 'E', 1)
# Replace the temporary placeholder back to 'e'
new_name = temp_name.replace('TEMP', 'e', 1)
print("Modified name:", new_name)







# First Replacement:

# The first replace('e', 'TEMP', 1) replaces the first occurrence of 'e' with the temporary string 'TEMP'.
# This ensures that the first 'e' is no longer present in the string, allowing us to focus on the second occurrence.
# Second Replacement:

# The second replace('e', 'E', 1) now targets the second occurrence of 'e' (which is still present in the string) and replaces it with 'E'.
# At this point, the string has the first 'e' replaced with 'TEMP' and the second 'e' replaced with 'E'.
# Final Replacement:

# Finally, replace('TEMP', 'e', 1) replaces the temporary placeholder 'TEMP' back to 'e', restoring the first occurrence of 'e' while keeping the second occurrence as 'E'.
