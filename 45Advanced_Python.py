# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:27:51 2020

@author: Kajal
"""

# Advanced Numbers

hex(12)

bin(12)

2** 4
#OR
pow(2,4)

pow(2,4,3)   # (x**y) % z

abs(2)

round(4.5)

round(3.14159, 3)    # 2nd argument is for number of digits after decimal

# Advanced Strings

s = 'hello world'

s.capitalize()

s.upper()

s.count('o')

s.find('o')

# center method : (total length , in between what)
s.center(20, 'x')

print('hello\t hi')
# OR
'hello\thi'.expandtabs()

s = 'hello'
s.isalnum()   # checks all characters are alphanumeric

s.isalpha()

s.islower()

s.isspace()

s.istitle()

s.isupper()

'HELLO'.isupper()

s.endswith('o')
s[-1] == 'o'

s.split('e')

s = 'hihiihiihhhhiiiihihiihhiih'
s.split('i')

s.partition('i')

## Advanced Sets

s = set()
s.add(1)
s.add(2)
s

#s.clear()
#s

sc = s.copy()
sc
sc.add(4)
s
sc

#difference method
s.difference(sc)

s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)
s1

s

s.discard(2)
s

s1 = {1,2,3}
s2 = {1,4,5}
s1.intersection(s2)

s1.intersection_update(s2)
s1

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2)   # False:as it has common
s1.isdisjoint(s3)   # True

s1.issubset(s2)     # True
s2.issuperset(s1)   # True

s1.symmetric_difference(s2)

s1.union(s2)

s1.update(s2)
s1

## Advanced Dictionary
d = {'k1':1, 'k2':2}
# dict comprehension
{x:x**2 for x in range(10)}

{k:v**2 for k, v in zip(['a', 'b'],range(10))}

# iteration over keys, vales

for k in d.iterkeys():
    print(k)

d.viewitems()

## Advanced list

l = [1,2,3,4]
l.append(4)
l.count(10)

x = [1,2,3]
x.append([4,5])
print(x)

x.extend([4,5])  #append individually
print(x)

l.index(2)
l.insert(2, 'inserted at index 2')

l.pop()
l.pop(0)   #at index 0

l.remove(3)

l.reverse()
l.sort()




    
