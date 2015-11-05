#Purpose: Write app that someone may use to keep track during baseball game

#For every pitch you'll need to record if it was a ball or strike or a hit.  You'll need to track outs and innings and runs scored.  To make tracking the runs scored easier you can assume all the hits are home runs.  At any point you should be able to print out the box score that shows how many runs were scored in each inning.  Also at any point you should be able to print out a game summary that is just a chronological list of what happened during each at bat.





# define requirements

# allow scorekeeper to record pitch
# system should determine innings, outs, and score.
  # all hits equate to hr 
# print out summary at any time
  #=================
 #Top 1st
 #==================
 #J. Hill struck out with 2/3 count
 
 
 
# print out box score at any time
     #      1 | 2 | 3 | ... R | H | E
  # Team 1    |   |   |
  # Team 2    |   |   |


# outline solution
#Step 1 allow to record pitch
 # ask user result of pitch
# pitch_count = 0

s = 0
b = 0
h = 0
o = 0
i = 1
i_side = 'Top'
summary = []


while True:
    # record result
    pitch = raw_input('What is the result of the pitch? (b)all (s)trike (h)it (p)rint (q)uit to exit ')
    pitch = pitch.lower().strip()

    # print 'The ball was a {}.'.format(pitch)
    if pitch == 's':
        s += 1
        if s == 3:
            o = o + 1
            print 'There is {} out(s)'.format(o)
            # reset pitch after out or walk
            b = 0
            s = 0
            
                  
    elif pitch == 'b':
        b += 1
        if b == 4:
            b = 0
            s = 0
    
    
    elif pitch == 'h':
        h = h + 1
        #print 'The hit count is {} '.format(h)

    elif pitch == 'p':
        for s in summary:
            print s


    else:
        pitch == 'q'
        print "You're no fun"
        break
        
    
    
 # keep track of inning to bottom/top after three outs
    if o == 3:
        b = 0
        s = 0
        i += .5
        o = 0
        # print 'Before', i
        #i += (1/2)
        # print 'After', i
        # top when int/bottom when float
     
    
    if i == int(i):
        i_side = 'Top'
    else:
        i_side = 'Bottom'
        
    message = 'The strike count is {} and the ball count is {}, there is {} hits, and there is {} out(s) in the {} of the {} inning'.format(s, b, h, o, i_side, int(i))


    if pitch != 'p':


        summary.append(message)
#print out summary of balls and strikes at this point and at any time

        print message

    # for p in pitch:
    #     if pitch == 's':
    #         summary.append({'strike_count': s, 'pitch_count': +1})
    #     elif pitch == 'b':
    #         summary.append({'ball_count': +1, 'pitch_count': +1})
    #     else:
    #         summary.append({'hit_count': +1, 'pitch_count': +1})
    # print summary



    
#Also print box score at any time throughout
  #  keeps track of pitch, s, b, h
   ## ** so can print out at any time throughout 
   # use box_score list and dict that keeps track of all the s, b, o, i, etc
     ## create runner so whenever 4 balls occur and there is hit throughout (1/2)inning-adds to h which is teams total 
    
    



  # step 2 process result

  #out
  # if 3 strikes
  
  # inning/ run/ at bat summary

# step 3 be able print summary

# step 4 box score printing



#code to the outline







