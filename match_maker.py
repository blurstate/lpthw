#Purpose: Match Maker.  Write a program that contains the profile of a man.  It should have at least 5 characteristics like name, age, hair color, has kids, etc.  Get creative. Use as many data types (string, int, list, etc) as you can for the characteristics.

#Step1: Gather in requirements for man
# class Man(object):
#     def __init__(self):
#         self.name = ''
#         self.pets = ''
#         self.age = 0
#         self.political_views = ''
#         self.sexual_orient = ''


man = ['adam','yes', 23, 'right','heterosexual']
#Step2: Ask female for input of same requirements
user = []

#Step2: Ask name
name = (raw_input('What is your name? '))
#Step3: Ask if has pets
pets = (raw_input('Do you have any pets? '))
#Step4: Ask age
age = (raw_input('How old are you? '))
#Step5: Ask which way do you lean when voting
political_views = (raw_input('Which way do you lean when voting? ')) 
#Step6: Ask sexual orientation
sexual_orient = (raw_input('What is your sexual orientation? '))

#put those items in list

user.append(name)
user.append(pets)
user.append(age)
user.append(political_views)
user.append(sexual_orient)

print user

#Step3: if female answered 50% of questions == male
#Step4: print out you are a match


#Just seeing if they would equate while using same input from user i.e. ==
# if user == man:
#     print 'You are a match'
# else:
#     print 'You are not a match'

#Now, have the program ask the user for their info for the same characteristics.  If their answers match at least half of the answers of the man already in the program, tell them they are a match.

