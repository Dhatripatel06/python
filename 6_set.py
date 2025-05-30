s1 = {'p','q','r'}
s2 = {'q','r','s'}
print(s1)
# add element in set
s1.add('t')
s1.add('r')

s1.remove('r') # remove element from set
print(s1)
s1 = {'p','q','r'}
s2 = {'q','r','s'}

print(s1.intersection(s2)) #  element from both set  unique only
print(s2.intersection(s1)) #  can not change set position 
print(s1.union(s2)) #  all element but unique only
print(s2.union(s1)) #  can not  change set position 
print(s1.difference(s2)) # unique value from set 1
