import requests

class Make():
    name = ''
    years = []
    
    def __init__(self):
        self.name = ''
        self.years = []
    
makes = {}
years = []
    
base_url = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'
year_param = 'modelyear'
make_param = 'make'


# get all years
r = requests.get(base_url)
year_json = r.json()
for year in year_json['Results']:
  years.append(year['ModelYear'])
 

# loop through years adding makes to dictionary
for y in years:
    url = '{}/{}/{}'.format(base_url, year_param, y)
    url = 'http://www.nhtsa.gov/webapi/api/SafetyRatings/modelyear/{}?format=json'.format(y)
    r = requests.get(url)
    makes_json = r.json()
    
    for r in makes_json['Results']:
        make = r['Make']
        if make not in makes:
            print y, 'adding', make
            m = Make()
            m.name = make
            makes[make] = m
            
        m = makes[make]
        if y not in m.years:
            m.years.append(y)
            
            
for m in makes.values():
    m.years = sorted(m.years)
    
    print m.name, m.years[0], m.years[-1]

            

# print each make and years