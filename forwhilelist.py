# for, while, list
# Purpose: Keep asking me my age until I tell you I'm 29, tell me how many times it took.
#Step1: ask how old you are
#ask_count = 0
# age = ''
# ask_count = 0
# #step2: Decide if age is 29
# while age != 29:
#     age = int(raw_input('How old are you?'))
#     ask_count = ask_count + 1
# #Step4: List number of times it took until you said 29
# print 'How many times it took is {}'.format(ask_count)



# Purpose: Ask my my age 5 times
#Step1: ask your age
# age = ''
# ask_count = 0
# #step2: repeat 5 times
# while ask_count != 5:
#     age =int(raw_input('How old are you?'))
#     ask_count = ask_count +1


# Purpose: Ask me my age 5 times or until I tell you I'm 29, tell me how many times it took.
#Step1: ask age
# age = 0
# ask_count = 0
#
# #Step2: decide if you were 29 or  decide if count was 5 or not
# for ask_count in range(1, 6):
#     age = int(raw_input('How old are you?'))
#     if age == 29:
#         break
# print 'It took {} times'.format(ask_count)
#
# # while True:
#     if age == 29:
#         break
#     if ask_count == 5:
#         break
#     age = int(raw_input('How old are you?'))
#     ask_count = ask_count + 1
# print 'It took {} times'.format(ask_count)
  
        
#Step3: tell how many times took 




# Purpose: Print out every even number from 1 to 100, tell me how many there are.
#Step1: list numbers 1 to 100
numbers = 0
even_numbers = numbers + 2
#Step2: pick out of list even numbers
for numbers in range(2, 99):
    even_numbers = numbers + 2
    print 'The number next in range from 1 - 100 is {}'.format(even_numbers)
#Step3: range***




# Purpose: Divide every number from 1 to 100 by 3 and print out the remainder of that division operation.  Tell me how many have a remainder of 2
#Step1: list divisor
# number = 0
# divisor = 3
# #remainder = number/divisor
# #Step2: Have divisor cycle through 1 - 100
# for number in range(1, 101):
#     remainder = (number/divisor)
#     print ' {} divided by {} equals {}'.format(number, divisor, remainder)
#
#     #if remainder == 2:
# print number
    
#Step3: print out 1/3 - 2/3 - 3/3 ... etc..
#Step4: cycle through list picking out the numbers w/ remainder of two




# # Purpose: Tell me what foods I said I liked.
# #Step1: Find out list of foods you like
# food_that_you_like = [raw_input('What kind of food do you like?')]
# #Step2: Tell you the foods you like
# for food in food_that_you_like:
#     print 'You said you liked ' + food
# #Step3: Cycle through list
#
#


# # Purpose: Tell me which foods that you and I both like.
# #Step1: Tell which foods I like
# food_that_i_like = ['banana', 'steak', 'chicken', 'burgers']
# #Step2: list foods you like
# food_that_you_like = [raw_input('What kind of foods do you like?')]
#
# #Step3: Compare lists
# #for food in food_that_i_like:
#     #print 'I want ' + food
# #Step4: Tell which foods you and I like
# for food in food_that_i_like and food_that_you_like:
#     print 'These are foods that you and I like ' + food
#
#     if food_that_i_like == food_that_you_like:
#         print 'These are the same'
#     else:
#         print 'These are the foods that you and I both like ' + food


#Step 1: find your age
# age = 0
# ask_count = 0
# #Step 2: decide if age is 29
# while age != 29:
#     age = int(raw_input('How old are you?'))
# #Step 3: keep track of times taken
#     ask_count = ask_count + 1
# #Step 4: print taken
# print 'This took {} time(s)'.format(ask_count)

# #Ask age
# age = 0
# legal_drinking_age = 21
# age = int(raw_input('How old are you?'))
# years_until = 21 - age
# years_that_you_could = age - 21
# #Define legal drinking age
# #Decide if age is old enough to drink
# #If not, state how many years
# if age >= legal_drinking_age:
# #Tell if you are old enough to drink
#     print 'You are old enough to drink when you are {}'.format(legal_drinking_age)
#     print 'You have been drinking since {} years ago'.format(years_that_you_could)
# else:
#     print 'You are not old enough'
#     #If not, state how many years until
#     print 'You still have {}'.format(years_until)











