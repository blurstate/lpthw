#create a progam that will read a string of text. and count out how many words are used and there frequency. then print out the work and how many times it was used. 




import operator

def sortandcount(words):
	# manipulate the text so that the words can be put into a list and no puncuation exists"
	words=words.lower().strip()
	words=words.replace("'", " ")
	words=words.replace(".", " ")
	words=words.replace("?", " ")
	words=words.replace(",", " ")
	words=words.replace('"', " ")
	words=words.replace('!', " ")
	words=words.replace('--', " ")
	words=words.replace(')', " ")
	words=words.replace('(', " ")
	words=words.replace('*', " ")
	words=words.replace(':', " ")
	words=words.replace(';', " ")
	words=words.replace('/n'," ")

	#print words
	words=" ".join(words.split())
	words= words.split(' ')  #move words into a list 

	words=sorted(words)


	#move through the list and put any new words into a dictionary that will have a counter attached to it for each word
	sorttedwords= {}
	wordcount=1
	newwords=0



	#words= ["the", "the", "a", "a", "jackson", "jack", "answer", "answer", "answer", "jackson"]

	saveword=0
	for i in words:
		#print i, "==" , saveword, "count=", wordcount

		if i == saveword:
			wordcount += 1
			sorttedwords.update({ i : wordcount})
		else:
			wordcount = 1
			sorttedwords.update({ i : wordcount})
		saveword = i


	sorttedwords = sorted(sorttedwords.items(), key=operator.itemgetter(1))
	
	return (sorttedwords)
	

#test=sortandcount(scrape)
	
#for k, v in test:
#	print k,":",v



