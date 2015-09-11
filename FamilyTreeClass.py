#Classes like Modules
#Class-way of grouping functions and data, placing inside container so access w/ dot(.) operator

#Mini-Module
# w/ Class having people() function inside it
#Classes instead of modules- take class and use craft many, millions, and WILL NOT interfere w/ each other
#Import Module-only room for one in entire program*unless do hacks


class People():
    name = ''
    spouse = None
    age = 0
    children = []
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__()

# py crafts empty object() using def
# __init__ = "magic function"-calls function to initialize empty object
# self makes (empty object) and set variables just like D, M, etc...
# Took the example tangerine and set to song lyric and then initialized object
# Py takes new object and assigns it to "thing" variable for us to work with

parent = People ()
parent.spouse = People()

parent.name = raw_input("What is your name? > ")
parent.spouse.name = raw_input("What is your spouse's name? >")

num_children = int(raw_input('How many children do you have? > '))

for x in range(0, num_children):
    kid = People()
    kid.name = raw_input('What is your kids name {}? >' .format(x+1))
    parent.children.append(kid)
     
print '{} and {} have {} children'.format(parent.name, parent.spouse.name, num_children)
print "They are ..."

for c in parent.children:
    print '{n} age {a}'.format(n=c.name, a=c.age)

###Not giving you class, but using class as blueprint for buliding copy####
#####Class is creating object and importing it at same time########
##Resulting in object and then assign variable for it to work with##

print parent
print parent.children
print parent.children[0]