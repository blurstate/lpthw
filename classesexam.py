# #Purpose: Tell me if I'm old enough to drink
# #Step1: Find your age
# age = int(raw_input('How old are you?'))
# #Step2: Find drinking_age
# drinking_age = 21
# #Step3: Tell if old enough to drink
# if age >= drinking_age:
#     print 'You can drink'
# else:
#     print 'You cannot drink'
    
#Purpose: Tell me if old enough to drink using Class
#Step1: define class of person
age = int(raw_input('How old are you?'))
class Person(object):
#Step2: find age of person
#Step2.1: def function inside of class
    def __init__(self):
        self.age = 0
#Step3: find drinking age
#Step3.1: Define function of drinking age inside of class
    def can_drink(self):
        return self.age >= 21
    if age >= can_drink:
        print 'You can drink'
    else:
        print 'You cannot drink'
        
        
