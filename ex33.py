def ex_33(Pass_1,Pass_2):
    i = 0
    numbers = []

    while i < Pass_1:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + Pass_2
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

ex_33(int(raw_input("Enter variable to test loop:")),int(raw_input("Enter number to increment by:")))
