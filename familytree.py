#ask the user their name
#ask them their spouces name
#aske the user houw many kids they have
#ask the name of each kid
#print all info out
parent={}


print "Hello, what is your name?"
parent['name']=raw_input(': ')
print "What is your spouces name?"
parent['spouce']=raw_input(': ')

print "How many kids do you have?"
numkid=input(": ")

i=0
while i<numkid:
    parent['kid %d' %(i+1)]= raw_input("Kid %d's name?:" %(i+1))
    i+=1
i=0

print"\n \n"
print "Ok so your name is: %s" % parent['name']
print "Your spouce's name is: %s" %parent['spouce']

while i<numkid:
    print"Kid %d is: " %(i+1), parent['kid %d' %(i+1)]
    i=i+1
    


