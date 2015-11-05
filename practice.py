# Ask me 
class Person(object):
    def __init__(self):
        self.age = 0
        self.gender = ''
        self.name = ''
   
    def can_vote(self):
        cv = self.age >= 18
        return cv
    #you can call this on class itself,
    @staticmethod
    def invalid_gender(gender):
       vg = gender not in ('male', 'female')
       return vg
     
        


#class is just fancy var
# age = int(raw_input('How old are you? '))
# gender = (raw_input('Are you male or female? '))
# name = (raw_input('What is your name? '))

male_count = 0
female_count = 0
people = []

#print p.name, p.age, p.gender

while (male_count < 1) or (female_count < 1):
    age = int(raw_input('How old are you? '))
    gender = ''
    name = (raw_input('What is your name? '))
    voting_age = 18
    
    while Person.invalid_gender(gender):
        gender = (raw_input('Are you male or female? '))
    
    p = Person()
    p.age = age
    p.gender = gender
    p.name = name
   
    
    people.append(p)
    
    if gender == 'male':
        print 'Your name is {}'.format(name)
        if p.can_vote():
            print 'You can vote'
        else:
            print 'You can NOT vote'
        male_count = male_count + 1
        
    elif gender == 'female':
        print 'Your name is {}'.format(name)
        if p.can_vote():
            print 'You can vote'
        else:
            print 'You can NOT vote'
        female_count = female_count + 1
        print male_count, female_count
print people
def saying_vote():
        if p.can_vote():
            voting_elig = 'can'
        else:
            voting_elig = 'cannot'
        print 'Your name is {} and you {} vote'.format(p.name, voting_elig)
for p in people:
    if p.gender == 'female':
      saying_vote()  
    
        
for p in people:
    if p.gender == 'male':
        saying_vote()



    #if p.gender == 'female':
        #print p.name
        #print p.age >= voting_age
        # if p.can_vote():
 #            voting_elig = 'can'
 #        else:
 #            voting_elig = 'cannot'
 #
        #female_count = 1
        
        # print 'Your name is {} and you {} vote'.format(p.name, voting_elig)
    #else:
        #if p.can_vote():
            # voting_elig = 'can'
        # else:
#             voting_elig ='cannot'
#         print 'Your name is {} and you {} vote'.format(p.name, voting_elig)
    
    
     
    
    
       

    


        