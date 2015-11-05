import requests

class Make():
    name = ''
    years = []

    def __init__(self):
        self.name = ''
        self.years = []


makes = {}
years = []

apiUrl = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'
apiParam = ''
outputFormat = "?format=json"

url = apiUrl + apiParam + outputFormat

print url

r = requests.get(url)
year_json = r.json()
for year in year_json['Results']:
    years.append(year['ModelYear'])
    #print year['ModelYear']

for y in years:
    url = '{}/{}/{}'.format(apiUrl,'ModelYear',y)
    r = requests.get(url)
    makes_json = r.json()
    #print url

    for r in makes_json['Results']:
        make = r['Make']
        if make not in makes:
            #print y, 'adding', make
            m = Make()
            m.name = make
            makes[make] = m
        m=makes[make]

        if y not in m.years:
            m.years.append(y)

for m in makes.items():
    m.years = sorted(m.years)
    print m.name, m.years[0], ' - ', m.years[-1], '\n'
