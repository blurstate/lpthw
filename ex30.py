p = 30
c = 40
t =15

if c>p:
    print "We should take the cars."
elif c<p:
    print "We should not take the cars."
else:
    print "We can't decide."
    
if t>c:
    print "That's too many trucks."
elif t<c:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
    
if p>t:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then." 
