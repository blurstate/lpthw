word_number = int(raw_input('How many words do you want to translate?'))

for i in range(word_number):

	original = raw_input('Enter a word:')

	if len(original) > 0 and original.isalpha():
		print 'Alright, your word in PygLatin is:' 
	else:
		print "That's not a word dumbass"
    
	pyg = 'ay'
	
	word = original.lower()

	first = word[0]

	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]

	print new_word