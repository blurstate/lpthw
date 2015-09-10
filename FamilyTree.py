parent = {'name': '', 'spouse': '' , 'children':[] }

name = " What is your name?"
spouse = " What is your spouse name?"
kid = " What is your kid's name?"
number = "How many children?"

parent['name'] = raw_input(name)
parent['spouse'] =raw_input(spouse)

parent['number'] = int(raw_input(number))


for x in range(0, parent['number']):
 k = {}
 k['name'] = raw_input(kid)
 
 parent['children'].append(k)

print parent