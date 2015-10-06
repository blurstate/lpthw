import sqlite3
import requests
import mechanize
from BeautifulSoup import BeautifulSoup

conn = sqlite3.connect('store.db')
print "Opened database succesfully"

#conn.execute('''CREATE TABLE STORES
#	(STORE_NUMBER INT PRIMARY KEY NOT NULL,
#	ADDRESS 			TEXT NOT NULL);''')
	
#print "Created table succesfully"

store_num = 100

for store_num in range(108,111):

	site = 'http://www.walmart.com/store/'

	url = (site + str(store_num) + '/details')	
	print url

	response = requests.get(url)

	html = response.content


	soup = BeautifulSoup(html)
	address = soup.find('div', attrs={'class': 'mobile-name-address pull-left'})
	#print soup.prettify()

	#print address
	
	
	try:
		for div in address.findAll('div'):
			text = div.text
			print text
		
	except AttributeError:
		print "Invalid store number"
		3
		try:
			conn.execute("INSERT INTO STORES(STORE_NUMBER, ADDRESS) VALUES (?, ?)", (store_num, text))
			
			conn.commit()
			print "Records created succesfully"
		except sqlite3.IntegrityError:
			print "Store number is not unique"
			
conn.close()
	