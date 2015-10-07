# ask users name
# ask users spouse name
# ask how many kids
# ask kids names and ages
# print all names
# 
# 

class people():
	name = ''
	spouse = None
	age = 0
	children = []

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

parentname = people()
parentname.spouse = people()

parentname.name = raw_input('What is your name? > ')

parentname.spouse.name = raw_input("What is your spouse's name? > ")

num_children = int(raw_input('How many kids do you have? > '))

for i in range(0, num_children):
	child = people()
	child.name = raw_input('Whats the name of the child {}? > '.format(i+1))
	child.age = int(raw_input('Whats the age of the child {0} > '.format(i+1)))
	parentname.children.append(child)


print '{} and {} have {} children'.format(parentname.name, parentname.spouse.name, num_children)
print 'They are ...'

for c in parentname.children:
	print '{n} age {a}'.format(n=c.name, a=c.age)


print parentname
print parentname.children
print parentname.children[0]





#
# parent = {'name': '', 'spouse': '', 'children': []}
# 
# parent ['name'] = raw_input('what is your name? ')
# parent['spouse'] = raw_input('what is your spouse name? ')
# num_children = int(raw_input('how many children do you have? '))
# 
# for i in range(0, num_children):
# 	child = {}
# 	child['name'] = raw_input('what is the name of child {}')
# 	child['age'] = int(raw_input('what is the age of child {0}')
# 	
