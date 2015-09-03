# imports argv command from sys MODULE
from sys import argv
# sets script and filename as values for argv to unpack
script, filename = argv
# command to open 
txt = open (filename)
# prints string then reads and displays the said file
print "Here's your file %r:" % filename
print txt.read()

