#Purpose: Tell me which of my kids can drink
#Step1: find kids ages
kids_ages = {'kid1': 19, 'kid2': 23, 'kid3': 22, 'kid4': 17}
#Step2: set drinking_age var
drinking_age = 21
#Step3: cycle through kids ages until pull out the ones that can drink
for kid, age in kids_ages.iteritems():
    #print age >= drinking_age
    if age >= drinking_age:
        print '{} can drink like a fish'.format(kid)
    else:
        print '{} cannot drink'.format(kid)
    
#Purpose: Tell me which of my pets are dogs
#Step1: Find pets
pets = {'pet1': 'cat', 'pet2': 'dog', 'pet3': 'rabbit', 'pet4': 'dog'}

#Step2: Cycle through list of pets until find dogs
for animal, pet in pets.iteritems():
    print 'Your {} is a {}'.format(animal, pet)


#Purpose:
#Tell me the names of kids that have dogs who are labs
#Step1: Find kids names who have dogs
kids_who_have_dogs = {}
kids_who_have_dogs["Adam"]=""
#Step2: Eliminate kids whose dogs are not labs

#Step3: print list of kids names who have dogs that are labs

