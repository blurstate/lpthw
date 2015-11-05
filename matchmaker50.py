# Step 1: Ask the man for characteristics.
m_gender = (raw_input('Are you male or female? '))
m_name = (raw_input('What is your name? '))
m_pets = (raw_input('Do you have any pets? '))
m_age = int(raw_input('How old are you? '))
m_political_views = (raw_input('Which way do you lean when voting? '))
m_sexual_orient = (raw_input('What is your sexual orientation? '))


print 'So your name is {}'.format(m_name)

# Step 2: Ask the woman for the same characteristics.
#name, pets, etc..

gender = (raw_input('Are you male or female? '))

w_name = (raw_input('What is your name? '))
w_pets = (raw_input('Do you have any pets? '))
w_age = int(raw_input('How old are you? '))
w_political_views = (raw_input('Which way do you lean when voting? '))
w_sexual_orient = (raw_input('What is your sexual orientation? '))

print 'So your name is {}'.format(w_name)


# Step 3: Compare their answers.
# Step 4: Keep a tally of only the ones they both answered the same.
identical_answers = 0

if (gender == 'male') or (gender == 'female'):
    #continue
    
    if m_name == w_name:
        identical_answers = identical_answers + 1
    if m_pets == w_pets:
        identical_answers = identical_answers + 1
    if m_age == w_age:
        identical_answers = identical_answers + 1
    if m_political_views == w_political_views:
        identical_answers = identical_answers + 1
    if m_sexual_orient == w_sexual_orient:
        identical_answers = identical_answers + 1


# Step 5: If the tally is greater than or equal to 50 % print they are a match.

if identical_answers >= 2.5:
    print 'You are a match to {}'.format(m_name)
else: 
    print 'You are NOT a match to {}'.format(m_name)