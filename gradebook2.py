# The python challenge for today is a Gradebook program.  Write a program that will check test scores of several students.  It should end by printing the average score for males and the average score for females.  You can hardcode the scores in the program rather than enter them in all the time with raw_input.  For bonus points, see if you can get python's random number generator to create the scores for you so the output will change every time you run it.
#
# Step1: Input male/female scores
import random

scores = []


    


# print random.randrange(0, 101)


scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'male', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})
scores.append({'gender':'female', 'score': random.randrange(60, 101)})

total_score = 0

for s in scores:
   total_score += s['score']
   if s['gender'] == 'male':
       average_male_score = total_score/len(scores)
   else:
       average_female_score = total_score/len(scores)      

    
#Average scores - sum and then number of scores

print 'The average male score is {} '.format(average_male_score)
print 'The average female score is {} '.format(average_female_score)




#print 'The average score for male students is {}'.format['score']

# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
#
#
# print 'The average score for male students is {}'.format(sum(male_scores)/len(male_scores))
#
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
# scores.append(random.randrange(60, 101))
#
# print 'The average score for female students is {}'.format(sum(female_scores)/len(female_scores))
#
#
# gender = (raw_input('Are you male or female? '))
#
# if gender == 'male':
#     male_score = int(raw_input('What was your score? '))
# #Add to list of male
#     male_scores.append(male_score)
#
#     print 'The average for the male student now is: '
#     print (sum(male_scores)/len(male_scores))
#
# else:
#     female_score = int(raw_input('What was your score? '))
#     female_scores.append(female_score)
#
#     print 'The average for the female student now is: '
#     print (sum(female_scores)/len(female_scores))
#
