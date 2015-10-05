import requests
import mechanize
import sqlite3
from mechanize import Browser
from bs4 import BeautifulSoup

conn = sqlite3.connect(':memory')
print 'Opened database successfully'
conn.execute('''DROP TABLE stores;''')
conn.execute('''CREATE TABLE STORES (number primary key not null, address not null, city not null, state not null, zipcode not null);''')

baseUrl = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myClub='
numStores = 0
storeNumber = 8149
count = 1

while count < 10:

	url = baseUrl + str(storeNumber)

	#print url

	mech = Browser()
	page = mech.open(url)
	html = page.read()
	
	#print page.code

	address = []
	soup = BeautifulSoup(html,'html.parser')
	#print soup.prettify()
	address = soup.find('div',attrs={'id':'HeaderClubAddress'})

	if address is not None:

		addressString = unicode(address.contents[0])
		#print addressString
		addressString = addressString[22:].encode('ascii','ignore')
		#print '%s -- %s' %(storeNumber,addressStringShort)
		streetAddress, remainder = addressString.split('|')
		city, remainder2 = remainder.split(",")
		state, zipcode = remainder2.split()
		#print '{} -- {} -- {} -- {}'.format(streetAddress, city, state, zipcode)
		conn.execute('''INSERT INTO stores(number, address, city, state, zipcode) values(?,?,?,?,?);''', (storeNumber,streetAddress, city, state, zipcode))
		#numStores += 1
	storeNumber += 1
	count += 1

c = conn.cursor()
c.execute('''SELECT * from stores''')
for row in c:
	print'Store Number: {} is at {}, {}, {} {}.'.format(row[0],row[1],row[2],row[3],row[4])
#print numStores
conn.close()
