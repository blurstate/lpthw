# The python challenge for today is a Gradebook program.  Write a program that will check test scores of several students.  It should end by printing the average score for males and the average score for females.  You can hardcode the scores in the program rather than enter them in all the time with raw_input.  For bonus points, see if you can get python's random number generator to create the scores for you so the output will change every time you run it.
#
# Step1: Input male/female scores
male_scores = [83, 99, 85, 93, 97, 74, 84]
female_scores = [83, 75, 90, 99, 92, 98, 74]


    
# Step2: doAvg for male and female students separately.
# Step3: print the avg of male and female
print 'The average for the male students is {}'.format(sum(male_scores)/len(male_scores))

print 'The average for the female students is {}'.format(sum(female_scores)/len(female_scores))


#Step4: *Bonus-just something I added on to add to list
#Establish gender and ask score
gender = (raw_input('Are you a male or female?'))

if gender == 'male':
    male_score = int(raw_input('What was your score? '))
#Add to list of male
    male_scores.append(male_score)
    
    print 'The average for the male student now is: '
    print (sum(male_scores)/len(male_scores))

else:
    female_score = int(raw_input('What was your score? '))
    female_scores.append(female_score)
    
    print 'The average for the female student now is: '
    print (sum(female_scores)/len(female_scores))
    

#Random Number generator

#random.randrange(0, 101)

     # male_scores.append(random.randrange)


