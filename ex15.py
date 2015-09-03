# imports argv command from sys MODULE
from sys import argv
# sets script and filename as values for argv to unpack
script, filename = argv
# command to open 
txt = open (filename)
# prints string then reads and displays the said file
print "Here's your file %r:" % filename
print txt.read()
# Prompts user to type in the filename again
print "Type the filename again:"
file_again = raw_input("> ")
# opens whatever file the user has typed in
txt_again = open(file_again)
# displays the file 
print txt_again.read()