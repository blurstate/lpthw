# Dictionary
# Map one thing to another
# Get X from Y

mystuff = {'apple': "I am apples!"}
print mystuff['apple']

# Modules
# Py with some functions/variables in it
# Import
# Access the func/var in module w/ . (dot) operator

# Ex
# this goes in mystuff.py
def apple():
    print "I am Apples!"
# Once code is written, use the module mystuff with import and then access apple function
import mystuff
mystuff.apple()
#Access variables like this:
def apple():
    print "I am apples!"
#Var#
tangerine = "Living reflection of a dream"
#Access same way
import mystuff

mystuff.apple()
print mystuff.tangerine

#Dict/Module/Variable
mystuff['apple'] #D get apple
mystuff.apple() #M get apple
mystuff.tangerine #V get apple

#Very common pattern 
#1:Take a key=value style container
#2:Get something out of it by key name

#Classes like Modules
#Class-way of grouping functions and data, placing inside container so access w/ dot(.) operator

class MyStuff(object):
    
    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print "I am classy apples"
#Mini-Module
# w/ MyStuff having apple() function inside it
#Classes instead of modules- take MyStuff class and use craft many, millions, and WILL NOT interfere w/ each other
#Import Module-only room for one in entire program*unless do hacks

#Class has similar concept to #import#
###Instantiate##=create
#You call the class like it's a function
thing = MyStuff()
thing.apple()
print thing.tangerine
###Breaking it down###
#1 py looks through MyStuff and sees that it is a class that youve defined
#2 py crafts empty object() using def
#3 __init__ = "magic function"-calls function to initialize empty object
#4 self makes (empty object) and set variables just like D, M, etc...
#5 Took the example tangerine and set to song lyric and then initialized object
#6 Py takes new object and assigns it to "thing" variable for us to work with

###Not giving you class, but using class as blueprint for buliding copy####
#####Class is creating object and importing it at same time########
##Resulting in object and then assign variable for it to work with##

#Dict style:
mystuff['apples']

#Module style:
mystuff.apples()

#Class style
thing = MyStuff()
thing.apples()
print thing.tangerine

###########
   