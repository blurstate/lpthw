words = u"""

"""
#Gather list of words


words = words.lower.split(' ')
#Split words by space


wordCount = {}
#Add dict to store items, found in string 

#for the number of times a word shows up in the count, add 1 to the specific word
#move on in count until cycle through end

for w in words:
    if w not in wordCount:
        wordCount[w] = 0
    wordCount[w] += 1
    
#print wordCount with each item listed alpha

#len of each word-basically the same thing as above, but instead of tracking word track length. 
