# Age = int(raw_input('How old are you?'))
# Gender = (raw_input('What is your gender?'))
#
# if (Age  >= 15 and Gender == 'Male') or (Age >= 50 and Gender == 'Female'):
#     print 'Old enough to date'
#     #print 'You are not'
#
#  #Age >= 50 and Gender == 'Female':
#
#         # print 'Old enough to date'
# else:
#     print 'You are not old enough to date'
    
    
# Married = raw_input('Are you married or not?')
#
# if Married == 'Yes':
#     print 'You are married'
# else:
#     print 'You are not married'

#Step 1: Ask me age
# age = int(raw_input('How old are you?'))
# #Step 2: Define drinking age
# drinking_age = 21
# #Step 3: Subtract drink from age
# num_years = drinking_age - age
#
# #print Drink - Age
#
# if num_years < 0:
#     print 'You are old enough to drink already'
# else:
#     print 'You have {} years left'.format(num_years)

###variables should never start with capital
##classes start w/ capital


# age = int(raw_input('How old are you?'))
# smoking_age = 18
# years_till_legal = smoking_age - age
# years_legal = age - smoking_age
#
# if years_till_legal < 0:
#     print 'You have been able to smoke for {} years.'.format(years_legal)
# else:
#     print 'You have {} years left.'.format(years_till_legal)
#if age >= smoking_age:
        #print 'You have been able to smoke for {} years.'.format(legal) 
    
#ask how old, if =>18 subtract smoking_age from age


#Step1: Are you married? (Y)
married = raw_input('Are you married?')

if married == 'Yes':
     print 'Congrats'
#No continue
elif married == 'No':  #cannot have comparision in else

#Step2: How old? if not married
    age = int(raw_input('How old are you?'))
#Step3: Be of age >=18
    if age >= 18:
        print 'You can get married'
    else: 
        print 'You cannot get married'
#Step4:




  

    