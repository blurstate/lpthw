# for, while, list
# Purpose: Keep asking me my age until I tell you I'm 29, tell me how many times it took.
#Step1: ask age
# age = int(raw_input('How old are you? '))
# #keep tally
# ask_count = 1
# #if you didn't say 29 keep going until 29
# while age != 29:
#     age = int(raw_input('How old are you ? '))
#     #keep tally
#     ask_count = ask_count + 1
# print 'It took {} times for you to tell me you are 29'.format(ask_count)


# Purpose: Ask my age 5 times
#tally ask_count
# ask_count = 0
#
# #decide if ask_count exceeds 5
# while ask_count != 5:
#     age = int(raw_input('How old are you? '))
#     ask_count = ask_count + 1

# Purpose: Ask me my age 5 times or until I tell you I'm 29, tell me how many times it took.
#ask age and set ask_count = 1
#age = int(raw_input('How old are you? '))
#ask_count = 0

#Decide if I've asked you 5 times or if youve told me 29
# while (ask_count != 5) or (age !=29):
#     age = int(raw_input('How old are you? '))
#     ask_count = ask_count + 1
#     if age == 29:
#         print 'It took {} times for you to tell me your {}'.format(ask_count, age)
#


# Purpose: Print out every even number from 1 to 100, tell me how many there are.
#Step 1: Define number 
# number = 0
# num_count = 0
# #Step 2: Decide if numbers are even 1 - 100
# for number in range(1, 101):
#     if number % 2 == 0:
#         num_count = num_count + 1
#         print number
#
# print 'There are {} even numbers in the range from 1 - 100'.format(num_count)



########## Purpose: Divide every number from 1 to 100 by 3 and print out the remainder of that division operation.  Tell me how many have a remainder of 2#####3
## Step 1: define number
# number = 0
# #Step2: Define divisor
# divisor = 3
# #Step 3: Define remainder
# #remainder = number % 3
# remainder_two = 0
# #Step 4: Cycle through 1 - 100, dividing each n by 3
# for number in range(1, 100):
#     remainder = number % 3
#     #print number, remainder
#
#          ########################
# #Step 5: Print how many have remainder of 2
#     if number % 3 == 2:
#         remainder_two += 1
#         print number


# Purpose: Tell me what foods I said I liked.
##Step 1: Find foods that you like
# food_that_you_like = (raw_input('What kind of food do you like? '))
##Step1.5: Create list of foods that you like
# food = []
##Add foods that you like on to list
# food.append(food_that_you_like)
# #Step 2: print foods that you like
# print 'You said you liked {}'.format(food)


#List of food that 

Purpose: Tell me which foods that you and I both like.
Step 1: List foods that I like
food_that_i_like = ['steak', 'chicken','burgers', 'potatoes']
#Step 2: Find foods that you like
food_that_you_like = (raw_input('What kind of foods do you like? '))
food_you_like = []
food_you_like.append(food_that_you_like)
print food_you_like

#Step 3: Compare lists
for food in food_you_like:
    if food_you_like == food_that_i_like:
        print food

#Step 4: Cycle through lists picking out identical items



