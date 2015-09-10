#parent = {'name': '', 'spouse': '', 'children': []}
class Person():
    name = ''
    spouse = None
    age = 0
    children = []
    
    def __str__(self):
        return self.name
        
    def __repr_(self):
        return self.__str__()

parent = Person()
parent.spouse = Person()

parent.name = raw_input('What is your name? > ')
#parent.age = raw_input('What is your age? > ')
parent.spouse.name = raw_input("What is your spouse's name? > ")
#parent.spouse.age = raw_input("What is your spouse's age? > ")

num_children = int(raw_input('How many children do you have? > '))

for i in range(0, num_children):
    child = Person()
    child.name = raw_input('What the name of child {}? > '.format(i+1))
    child.age = int(raw_input('What the age of child {0}? > '.format(i+1)))
    parent.children.append(child)


print '{} and {} have {} children'.format(parent.name, parent.spouse.name, num_children)
print "They are ..."

for c in parent.children:
#    print '{name} age {age}'.format(c)
    print '{n} age {a}'.format(n=c.name, a=c.age)
    
print parent

print parent.children

print parent.children[0]