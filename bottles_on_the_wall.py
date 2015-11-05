# 99 Bottles on the wall
# GOAL
# Create a program that prints out every line to the song "99 bottles of beer on the wall." 
# This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.
#
# RULES
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.



bottles = int(raw_input('How many bottles are on the wall? '))


	
while True:


	print "%s Bottles of beer on the wall!" % (bottles)
	print "%s Bottles of beer!" % (bottles)
	print "Take one down and pass it around!"
	bottles -= 1
	print "%s Bottles of beer on the wall!" % (bottles)


	if bottles == 0:
		break
