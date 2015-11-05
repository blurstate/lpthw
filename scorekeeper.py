##In honor of the world series, today's exercise is to write a python app that someone might use to keep score during a baseball game.  

# For every pitch you'll need to record if it was a ball or strike or a hit.

# You'll need to track outs and innings and runs scored.

# To make tracking the runs scored easier you can assume all the hits are home runs.

# At any point you should be able to print out the box score that shows how many runs were scored in each inning.

# Also at any point you should be able to print out a game summary that is just a chronological list of what happened during each at bat.
##



# define requirements


# all hits are home runs

# track outs/innings/runs (system should be able to tell me what inning we are in etc)
# be able to print out the box score 
# Team 		| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | R | H | E |
# Home 		|
# Visitor	|
# how many runs were scored in each inning

# be able to print the game summary as a paragraph statement 
# ==============
#	Top First
# ==============
# * J.Hill struck out with 2/3 count
# * J.Noble Hit a HR




# allow score keeper to record pitch (ball/strike/hit)
# 1. Allow to record a pitch 
# ask the user the result of the pitch (ball/strike/hit)

strikes = 0
balls = 0
hits = 0
outs = 0
runs = 0
innings = 1.0

while True:

    # record the result
    pitch = raw_input('What is the result of the pitch? (B)all (S)trike (H)ome Run. (Q) to quit.  ')
    pitch = pitch.upper().strip()

    # 2. Process the result

    if pitch == 'S':
        strikes += 1


    elif pitch == 'B':
        balls += 1


    elif pitch == 'H':
        hits += 1

    elif pitch == 'Q':
        print "Goodbye"
        break

    else:
        print "{} is not a valid pitch. Enter B, S, H, or Q.".format(pitch)


    # outs (out = 3 strikes)
    # adds 1 to the outs list and clears the strikes and balls lists
    if strikes == 3:
        outs += 1
        strikes = 0
        balls = 0

    # 4 balls is a walk
    if balls == 4:
        strikes = 0
        balls = 0

    # run
    #

    # at bat summary
    #

    # inning

    # (3 outs per half inning)
    # top (first team)
    # bottom (second team)

    if outs == 3:
        outs = 0
        innings += .5

    print "Its the {} of the {} inning. There are {} Balls, {} Strikes, {} Hits, {} Outs, and {} Runs.".format(balls,
                                                                                                               strikes,
                                                                                                               hits,
                                                                                                               outs,
                                                                                                               runs)






    # 3. Print summary
    # 4. Print box score
