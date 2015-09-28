people = 40
cars = 40
trucks = 15

if not cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
    
if trucks > cars:
    print "that's too many trucks"
elif trucks < cars:
    print "maybe we could take the trucks."
else:
    print "we still can't decide"
    
if people > trucks:
    print "alright lets just take the trucks"
else:
    print "fine lets stay home then"
