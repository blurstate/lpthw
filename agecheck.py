i=0
agel=[21,23,5,26,27,20]

def agecheck(age):
    if age<21:
        print "Age %d: Can't drink!" % age
    else:
        print "Age %d: Can drink!" % age

while i<6:
    agecheck(agel[i])
    i+=1

i=0

