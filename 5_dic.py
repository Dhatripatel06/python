d1= {
    'name' : 'Dhatri',
    'number': 67,
    
}
print(d1)
d1['name'] = "D Patel" # update element using key
print(d1)


d1['number'] = "440"# add  the element by key and value 
print(d1)

#del d1['number']  # delete 
#print(d1)


# you can also add elements into empty dictionary 
 
d2 = {}

d2['name'] = "D Patel" # update element with key use
print(d2)


d2['number'] = "440"# add  the element through key and value 
print(d2)


d3 = d1.copy()  # create copy of dic
del d3['number'] # delete value 
print(d3)
print(d2.items()) # print all items
print(d2.keys()) #  keys as list

print(d2.values()) #  values as the list
print(d2)
d2.clear() # delete all element from dic 2
print(d2) # empty dic