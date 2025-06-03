l1=[67,55.5,'dhatri',6677,"patel",'False']
l2=[66.7,"apple",'True']

print(l1,l2) 
l2[1]='Apple' #  you can change wholw element but cant chang one word in element
print(l2)
print(l1[0:]) #default end of string
print(l1[:6]) #default start of string
print(l1[2:6]) #set start and end index 
print(l1[0:5]) 
print(l1[1]) #only one index


print(l1+l2) #concatination
print(l1*3) #repeat
l1[3]=False  #element chang
print(l1) 

l1.append('pinapple') # add element at the end of list
print(l1)
l1.extend(l2) # add list at the last of list
print(l1)

#print(l1);print(l2)


# del l1  or l2 can delet the whole list 

l1.remove(55.5)
print(l1)

print(l1.pop(4))
print(l1)

l2.clear()
print(l2)

print(l1.index(67))
print(l1)   


print(l1.count('dhatri'))
l3 = [5,76,67,50,34,6,56]
l4 =['abc','xyz','pdr',"stv"]
# sort()  #Sort items in a list in ascending order if all items are of same type 
# print(l1.sort()) # return error because data type is not same


print(sorted(l3))
print(sorted(l4))

l3.sort()
print(l3)
  
l3.reverse()
print(l3)   
l5 = l1.copy()
print(l5)

del l5
#print(l5)