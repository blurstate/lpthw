from sys import argv
from os.path import exists

script, ffile, tfile = argv

print "Copying from %s to %s" % (ffile, tfile)

# we coudldo these two on one line, how?
#   indata=open(ffile).read()

ifile=open(ffile)
indata = ifile.read()  #move the .read up after the open function


print "the input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" % exists(tfile)
print "Ready, hit RETURN to continure, CTRL-C to abort."
raw_input()

outfile=open(tfile, 'w')
outfile.write(indata)

#simple mode    open(tfile, 'w').write(indata)

print "Alright, all done."

outfile.close()   # tell it to close tfile now
ifile.close()       #tell it to close indata now
