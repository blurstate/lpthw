#Figure out how old you are
# age = int(raw_input('How old are you?'))
# #Define the drinking age
# drinking_age = 21
# #tell if old enough to drink
# if age >= drinking_age:
#     print 'You have been drinking for {} years'.format(age-drinking_age)
# else:
#     print 'You can drink after {} years'.format(drinking_age-age)



#####Tell me which of the following I am allowed to do.  Drink, smoke, date.  If I'm not able to do any of them, tell me how many more years until I can.

Step1: Ask your age
age = int(raw_input('How old are you?'))
#Step2: Define Drinking age, smoking age, dating age.
drinking_age = 21
smoking_age = 18
dating_age = 15
#Step4: If not of dating age, assume not of smoking/drinking
if age <= dating_age:
    print 'You can not drink, smoke, or date'
else:
    print 'You can date now'
#Step5:Tell how many years until you can
    if age >= drinking_age:
        print 'You can smoke like a chimney, get as drunk as a skunk, and you have my permission to date.'
    else:
        print 'You may be able to date and smoke, but not drink'
        if age



#Tell me if I can smoke or drink
# #Step1:Define age
# age = int(raw_input('How old are you?'))
# #Step2:Define smoking/drinking age
# smoking_age = 18
# drinking_age = 21
# #Step3:If you are old enough to drink, then you can smoke
# if (age >= drinking_age) or (age >= smoking_age):
#     print 'You can smoke, but maybe not drink'
# else:
#     print 'You cannot smoke or drink'


#Tell me if i can smoke and drink
#Step1: Find out age
# age = int(raw_input('How old are you?'))
# #Step2: define drinking/smoking age
# drinking_age = 21
# smoking_age = 18
# #Step3: tell if you can drink,
# if (age >= drinking_age) and (age >= smoking_age):
#     print 'You can smoke and drink'
# else:
#     print 'Maybe you can smoke, but you cannot drink'
    



# #Tell me if I have the same name as you
# #Step1: Tell my name
# my_name = 'Jeremy'
# #Step2:Ask your name
# your_name = raw_input('What is your name?')
# #Step3: tell if you have same name as me
# if my_name == your_name:
#     print 'We have the same name'
# else:
#     print 'We do NOT have the same name, how sad'
    

####Tell me if we are same age
##Step1: tell my age
my_age = 24
##Step2: ask your age
your_age = int(raw_input('How old are you?'))
##step3: tell if we have same age
if my_age == your_age:
    print 'We are the same age'
else:
    print 'We are NOT the same age'
    



    
    