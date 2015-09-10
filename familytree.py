parent = {'name': '', 'spouse': '', 'children': []}


parent['name'] = raw_input('What is your name? > ')
parent['spouse'] = raw_input("What is your spouse's name? > ")
num_children = int(raw_input('How many children do you have? > '))

for i in range(0, num_children):
    child = {}
    child['name'] = raw_input('What the name of child {}? > '.format(i+1))
    child['age'] = int(raw_input('What the age of child {0}? > '.format(i+1)))
    parent['children'].append(child)


print '{} and {} have {} children'.format(parent['name'], parent['spouse'], num_children)
print "They are ..."

for c in parent['children']:
#    print '{name} age {age}'.format(**c)
    print '{n} age {a}'.format(n=c['name'], a=c['age'])
    
print parent

print parent['children']

print parent['children'][0]