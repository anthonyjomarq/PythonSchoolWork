# In class work
# Date: 11/9/2021

li = ['orange', 'apple', 'pear', 'banana', 'lemon']
vowels = ('a', 'e', 'i', 'o', 'u')

print(li)
counter = 0

for element in li:
    #if element[0] == "a" or element[0] ==  "e" or element[0] == "o" or element[0] ==  "u" or element[0] ==  "i" :
    if element[0] in vowels:
        li[counter] = element.upper()
        #print(element)
    counter += 1

print(type(li))
print(li)
