#this one is like your scripts wiht argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, thats *args is actualy pointless, we can jsut do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#this jsut takes one argumetns
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
    print "i got nothin'."
    
print_two("Zed", "Shaw")
print_two_again("Mac", "33")
print_one("First!")
print_none()
