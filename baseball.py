class Atbat():
	inning = 0
	batter = 0
	pitch = 0
	strikes= 0
	ball = 0 
	hit = 0    #if a ball is hit how many basses did they get?
	out = 0 #how did the batter get out? strike out, thrown out, or a fly ball catch, walk, or hit?
	runs = 0

scorecard=[]

for i in range(1,2):
	if i == 1:
		print "Its the 1st inning"
	elif i==2:
		print "Its the 2nd inning"
	elif i==3:
		print "Its the 3rd inning"
	else:
		print "Its the {}th inning".format(i)
		
	print "========================================"
	
	
	outs= 0 
	batter = 0
	while (outs < 3):
				
		batter += 1
		
		b=Atbat()
		b.inning = i 
		b.batter = batter
		print"Inning {}" .format(b.inning)
		print"batter #{}".format(b.batter)
		print"{} outs" .format(outs)
		pitch= 0
		while ( type(b.out) != str ):
			print" "
								
					
			pitch +=1
			b.pitch = pitch
			print "On pitch {} was it a ".format(b.pitch)
			print "1) strike?"
			print "2) ball?"
			print "3) hit?"
		
			x = input("Enter 1, 2, or 3:\n")
			if x==1:				
				b.strikes+=1
				print"STRIKE {}".format(b.strikes)
				if b.strikes==3:
					print"Strike out!"
					print"============================"
					outs+=1
					b.out="Stike out"
				
			elif x==2:
				b.ball+=1
				print"Ball {}" .format(b.ball)
				if b.ball == 4:
					b.hit += 1
					print"Walk on ball 4"
					if b.hit==4:
						b.hit= 0
						b.run+=1
						print "Walk for a run"
						print "==============================="
						b.out = "Walk for a run"
					
					b.out = "Walk"
				
				
			elif x==3:
				print"Hit"
				h=input("how many bases on the hit? \n")
				b.hit=h+holder
				holder=h
				while(b.hit >= 4):
					b.hit -= 4
					print"Run Scored"
					b.runs+=1
				print"==============================="
				b.out = "Hit"					
								
		if (type(b.out) == str):			
			scorecard.append(b)
								

for i in scorecard:
	print "inning", i.inning 
	print "batter", i.batter
	print "end of bat by" , i.out
	print "runs" , i.runs