# In class work
# Date:11/11/2021
import pprint

d={}

d['Italy'] = 'Rome'
d['France'] = 'Paris'
d['Spain'] = 'Madrid'
d['Mexico'] = 'CDX'

print(d)
print('better print')

pprint.pprint(d)

d['Spain'] = 'Barcelona'

print(d)
d['Spain'] = ['Madrid', 'Barcelona']

print(d)

for country, cities in d.items():
    print("The key is: ", country, " and value: ", cities)
for x in d.items():
    print("The key is: ", x[0], " and value: ", x[1])