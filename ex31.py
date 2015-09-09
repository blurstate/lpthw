print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("Enter 1 or 2:")

if door == "1":
    print """
        There's a giant bear here eating a cheesecake.
        \t1.\tTake the cake.
        \t2.\tScream at the bear.
        """
    bear = raw_input("Enter 1 or 2:")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print """
    You stare into the endless abyss at Ctuhulhus' retina.
    \t1.\tBlueberries.
    \t2.\tYellow jacket clothespins.
    \t3.\tUnderstanding revolvers yelling melodies.
        """
    insanity = raw_input("Enter 1 or 2 or 3:")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job."
