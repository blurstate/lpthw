# importing requests so use requests
import requests #when client asked server for data

# call year api
r = requests.get('http://www.nhtsa.gov/webapi/api/SafetyRatings?format=json')
#response object 
results = r.json() # what server sends back to client
#putting res into var called resputting
#print results.keys()

results = results['Results'] # getting value of results key-****list

#print results

years = []
makes2 = {}
for r in results: # loops 
    # print the value for the key that represents the year
    #print r['ModelYear']
    years.append(r['ModelYear'])
# years = list modelyear-key 
    
#print years

#single year
#Y integer
for y in years: #all the years


#Call make api

    r = requests.get('http://www.nhtsa.gov/webapi/api/SafetyRatings/modelyear/{}?format=json'.format(y))    #var
    makes = []
    makes = r.json()  
    makes = makes['Results'] # takes value 
    # print ma

    #makes list of dict
    for m in makes:
        m2 = m['Make'] #putting value of key into var
        #string
        makes2[m2]='' #dict has keys, access keys in []
#(Loading up makes to dict)
for m in makes2: #looping through the keys
    print m
#loop through dict, looks through keys.    

# m lastly is string
    
        
#
    





    
    










    

    
    
    
    
    

