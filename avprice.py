items={ 'gum':[.25, .40, 1.50, 1.25], 'candy': [.50,.60,1.00, 1.25, .65]}

# need code that will take the list and name from the dictionary and put it in to n> variable and li> list varibale

#n='gum'
#li=[.25, .40, 1.50, 1.25]

def avprice(dic):
    
    for name, price in dic.iteritems():
        a=0
        s=0
        for i in price:
            a=a+1
            s=s+i
            
        
        print 'The average price for {} is {}' .format(name,(s/a))
    
    
avprice(items)    
    
    
 #   print "Finding average prices for ", n
 #   a=0
  #  s=0
   # for i in list1:
    #    a=a+1
 #       s=s+i
 #     
        
  #  return s/a
    

#print avprice(n,li)   
