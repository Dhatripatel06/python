import random as r

print("random float number",r.random(),"-",r.random(),"-",r.random())


print ("float random number through uniform is " ,r.uniform(11,97))


print("random integer number",r.randint(1,200))


print("random number",r.randrange(4,200,40))

number_list= [89, 29, 34, 83, 52, 24, 34, 56, 90, 76]
print ("Original list : ", number_list)

r.shuffle(number_list) 
print ("List after the shuffle : ", number_list)

print (r.choices(number_list,k=2))

print (r.sample(number_list, 4))

