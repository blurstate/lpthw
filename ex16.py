from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you dont wnat that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodby!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

f=("%r\n%r\n%r\n") %(line1,line2,line3)
s=str(f)
target.write(s)
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#print "And then print it out"
#print target.read()

print "And finally, we close it."
target.close()



