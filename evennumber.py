#Purpose: Print out every even number going from 1 - 100
#
# #Step 1: Define number
# number = 0
#
# #Step2:Decide if numbers are even 1 - 100
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         print number
        
# #Purpose: Purpose: Tell me if I'm married or not.
#Ask if you are married
# married = (raw_input('Are you married? '))
#
# #If married, tell
# #If not, tell
#
# if married == 'yes':
#     print 'You are married.'
# else:
#     print 'You are not married.'

# Purpose: Tell me how many more years until I can drink or how many year's I've been able to.
# #Find age
# age = int(raw_input('How old are you? '))
#
# #Define drinking age
# drinking_age = 21
#
# how_long_until = drinking_age - age
# how_long_its_been = age - drinking_age
#
# #If not of age to smoke-tell how long until or tell how many years
# if age >= drinking_age:
#    print 'You have been drinking for {} year(s)'.format(how_long_its_been)
# else:
#     print 'You can drink in {} year(s)'.format(how_long_until)


# Purpose: Tell me how many more years until I can smoke or how many year's I've been able to.
#Ask age
# age = int(raw_input('How old are you? '))
#
# #Define smoking age
# smoking_age = 18
# #Define years until or years that have been able to
# years_until = smoking_age - age
# years_that_been_able = age - smoking_age
# #Tell how many years until or how long its been
# if age >= smoking_age:
#     print 'You have been destroying lungs for {} years'.format(years_that_been_able)
# else:
#     print 'You have {} years until you are legally allowed to take a drag off of a cancer stick'.format(years_until)

# Purpose: Tell me how many more years until I can date or how many year's I've been able to.
# #Define age
# age= int(raw_input('How old are you? '))
#
# #Define age that you can date
# dating_age = 16
# #Define eligibility in reference to age
# years_until_date = dating_age - age
# years_of_dating = age - dating_age
# #Tell how many years until or how many years you could have been
# if age >= dating_age:
#     print 'You could have been dating for {} years'.format(years_of_dating)
# else:
#     print 'You have to wait {} years until you even think about dating'.format(years_until_date)

# Purpose: Tell me if I can get married or not. (you can't get married if you are already married).
#ask age
# age = int(raw_input('How old are you? '))
#
# #Ask if married
# married = (raw_input('Are you married? '))
# #define age that you can get married
# age_of_eligibility = 18
# #Define years until you can get married
# years_until_eligible = age_of_eligibility - age
#
# #Tell if can get married or not
# if married == 'no' and age >= age_of_eligibility:
#     print 'You can get married'
# elif married == 'no' and age < age_of_eligibility:
#     print 'You can get married in {} years'.format(years_until_eligible)
# else:
#     print 'You are already married'



# Purpose: Tell me which of the following I am allowed to do.  Drink, smoke, date.  If I'm not able to do any of them, tell me how many more years until I can.
#Ask age
age = int(raw_input('How old are you? '))

#define drinking/smoking/dating age
dating_age = 16
smoking_age = 18
drinking_age = 21

years_until_date = dating_age - age
years_until_smoke = smoking_age - age
years_until_drink = drinking_age - age
#decide if age > dating_age
if age >= dating_age:
    print 'You can date'
else:
    print 'You have {} year(s) until you can date'.format(years_until_date)
#then smoking
if age >=smoking_age:
    print 'You can smoke and date'
else:
    print 'You have {} year(s) until you can smoke'.format(years_until_smoke)
#then drinking
if age >= drinking_age:
    print 'You can date, smoke, and drink'
else:
    print 'You have {} year(s) until you can drink'.format(years_until_drink)




# Purpose: Tell me if I can smoke or drink.
#Ask age 
# age = int(raw_input('How old are you? '))
# #Define drinking/smoking age
# drinking_age = 21
# smoking_age = 18
# #Tell if your age is old enough to drink or smoke
# if (age >= drinking_age) or (age >= smoking_age):
#     print 'You can smoke, but maybe not drink'
# else:
#     print 'You cannot smoke or drink'
#
#
# #ask age
# age = int(raw_input('How old are you? '))
# #Define smoking/drinking age
# smoking_age = 18
# drinking_age = 21
# # Purpose: Tell me if I can smoke and drink.
# if age >= smoking_age and age >= drinking_age:
#     print 'You can smoke and drink'
# else:
#     print 'You cannot smoke AND drink'





##  Purpose: Tell me if I have the same name as you.
# #Ask your name
# your_name = (raw_input('What is your name? '))
# #Define my name
# my_name = 'Jeremy'
# #tell if have same name
# if your_name == my_name:
#     print 'We have the same name'
# else:
#     print 'We do NOT have the same name'
#
# # Purpose: Tell me if we are the same age.
# #Ask how old you are
# your_age = int(raw_input('How old are you? '))
# #Define my age
# my_age = 24
# #Tell if same age
# if your_age == my_age:
#     print 'We are the same age'
# else:
#     print 'We are NOT the same age'
#
#
#
#












