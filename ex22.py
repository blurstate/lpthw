print "Hello world" #prints out text into the terminal
#  <==   excludes any text in this line after the # 

print "2+5=", 2+5 #print can also be used to print out the solution to a math problem 
v= 100
v2= 150
vs= v+v2 #variables can be declared and assinged values and even solutions of other variables 

print v,"+",v2, "=", vs #print can be used to print out whatever was assigend to the variable 

print "you can also show the value of vs like this = %d" %vs #%r,%s, %d can be used to place varibales inside you string of text r=force, s=string, d=digtis or numbers

print "{} + {} + {} = {}" .format(2,4,6,2+4+6) #can also be inserited like this with .format

print "How old are you?",
a=raw_input() #prompts user for input and asigins input to variable 

from sys import argv #user must input additional dadt or files to fill x number of givven variables in the program. first variable is always the program you are running 
a, b, c, d= argv

prompt="promting text"
pv= raw_input(prompt) #if you want the promt for input to desplay some text before prompting you can insert it with a variable or just text inside the ()

print """
this alows 
for multiple srings of words
without haveing to use the \n function 
to creat new lines
"""
# \n starts a new line when printing out text 

txt = open(filename) #have a pre exisitng variable with file name and use open() to assing it to a variable so that i can be read using 
print txt.read()  #in order to read a file it first has to be opened hince the mulitple varibales and not just using filename.read()

target=open(filename, 'w')#not sure what w does yet. need to ask <<<<<<<
target.truncate()  #this will clear the file. it still exist but whatever was in it gets errased 
line1= raw_input("write a line of text")
f=(line1,"\n",line1,"\n") #create a vairable to hold multiple lies of text 
s=str(f) #converts raw input into a string 
target.write(s) #writes the string (s) into the target file
target.close() #closes and saves the file 

len(file2) #gives the size of the file in bites
exists(file2) #checks to see if the file exist returns a bool true or falce 

copyfile.write(firstfile) #you can also use write with two seprate files to copy one to the other jsut make sure to open and close both 

def function(v1,v2,v3)      #def is used to define a function. functions are like complex variables. you can place them in the 
    print v1*3+v2/4-v3*6        #code and they will do whever was deffined in that function. you end the fucntion but undoing the indentation.
    
function(3,5,6) # this functions will print out the formula programed into it 
function(c2,c3,c4+3) # you can call variables or hard numbers into a function and even do math as well. it will asign the value to the pre defined variable
#you can also use .read() .wirte() ext in functinos. functions are basicly a minni program written inside your code that you plan to re use rather than having to type out again and again
what = add(age,subtract(height, multiply(weight, divide(iq,2)))) # you can even set funtions as an input for other functions 




