class parent():
    name=' '
    age= 0
    spouce= None 
    kids= []
    
 parent=parent()
 parent.spouce=parent()
 
 parent.name=raw_input("Your name? > ")
 parent.age=raw_input("Your age? > ")
 parent.spouce.name=raw_input("Your spouces name? > ")
 parent.spouce.age=raw_input("Your spouces age? > ")
 numkid=input("How many kids? >")
 
 for i in range(0,numkid)
    kid=person()
    kid.name=raw_input("Kid{} name? > ".format(i+1))
    kid.age=raw_input("Kid{} age? > ".format(i+1))
    parent.kids.append(kid)
    
print "Your name: {}" .format(parent.name)
print "Your spouce: {}" .format(parent.spouce.name)
print "You have {} kids together" .format(numkid)

    

