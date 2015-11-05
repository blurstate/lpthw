# outline solution
# Step (1) Allow to record a pitch
# ask user the result of the pitch (ball / strike / hit)

strikes = 0
balls = 0
outs = 0
inning = 1.0

def get_pitch():
    global balls
    global strikes
    global outs
    
    print "========================"
    print "==  Record the Pitch  =="
    print "========================"
    print "==   [B] - Ball       =="
    print "==   [S] - Strike     =="
    print "==   [H] - Home Run   =="
    print "==                    =="
    print "==   [Q] - Quit       =="
    print "========================"
    
    print "The count is {} balls and {} strikes.".format(balls, strikes)
    
    
    inning_side = 'top' if inning == int(inning) else 'bottom'
    print "There are {} outs in the {} of the {} inning.".format(outs, inning_side, int(inning))
    
    pitch = raw_input('? ')
    pitch = pitch.upper().strip()
    
    return pitch

def reset_at_bat():
    global strikes
    global balls
    
    strikes = 0
    balls = 0
    
def reset_inning():
    global inning
    global outs

    reset_at_bat()
    outs = 0
    inning += .5
  
def process_pitch(pitch):
    # Step (2) Process the result
      # outs
         # if 3 strikes then we have an out
      # inning
      # run
      # at bat summary

    global balls
    global strikes
    global outs
    global inning
    
    if pitch == 'S':
        strikes += 1

    elif pitch == 'B':
        balls += 1
    
    elif pitch == 'Q':
        print "Goodbye."
        return False

    else:
        print "{} is not a valid entry.  Enter B, S, H or Q.".format(pitch)
        
    # Out
    if strikes == 3:
        print "Strike Out !!!"
        outs += 1
        reset_at_bat()
        
    # Walk
    if balls == 4:
        print "Walk !!!"
        reset_at_bat()
        # TODO - put runner on base
        
    # Inning
    if outs == 3:
        reset_inning()
        
    return True
        
        
def main():
    global balls
    global strikes
    global outs

    while True:
        # record the result
        pitch = get_pitch()

        # process the result
        if not process_pitch(pitch):
            break


 
        # Step (2) Process the result
          # outs
             # if 3 strikes then we have an out
          # inning
          # run
          # at bat summary
   
    # Step (3) be able to print summary
    # Step (4) be able to print box score


if __name__ == "__main__":
    main()