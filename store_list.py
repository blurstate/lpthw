#purpose: copy store list from a company website to our database.

#Q: waht kind of data do we need
#	- store number
#	- store address
#	 -street, city, state, zip
#	- phone if available
#	- lat/long if available

#Q: waht geographic area
#	- all of the USA

#Q: what type of company
#	-big box style general merch retailser
#	- walmart, target, cvs, etc
#
#Q: what format (type of store). supercenter, market, etc.
#	-all

#execution plan
#1 find a website (target.com)
#2 find the store locator (footer, http://gam.target.com/store-locator/find-stores)
#3 learn how urls are structured http://gam.target.com/store-locator/sl/*/{}
#4 loop from 1 to 10000, requesting the store url
#	-assuming stores are numbered
#5 pull the address info from the html
#5.1 find the address
#	- find a div that contains the data
#	-slice the html starting at that div until the end of that div
#6 save to database

from urllib2 import Request, urlopen, URLError
import sqlite3


class Store(object):
	def __init__(self):
		self.number = -1
		self.street = ''
		self.city = ''
		self.state = ''
		self.postalCode = ''
		self.phone = ''

	@staticmethod
	def getAll(conn):
		cursor = conn.execute("SELECT * FROM STORES")
		for row in cursor:
			print "Store#: ", row[0]
			print "Street: ", row[1]
			print "City: ", row[2]
			print "State: ", row[3]
			print "Zipcode: ", row[4]
			print "Phone#: ", row[5], "\n"

		conn.close()




def main():
	
#	conn = sqlite3.connect('samsclub.db')
#	print "Opened database successfully"
#
#	conn.execute('''CREATE TABLE STORES
#		(STORE NUM INT PRIMARY KEY NOT NULL,
#			STREET 		TEXT	NOT NULL
#			CITY 		TEXT 	NOT NULL
#			STATE 		TEXT 	NOT NULL
#			ZIPCODE 	INT 	NOT NULL
#			PHONE 		INT 	NOT NULL);
#			''')
#	print "Created table successfully"
	print 'hello'

	url = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myClub={store_number}'

	for idx in range(4968, 4975):
		store_url = url.format(store_number=idx+1)
		print store_url
		request = Request(store_url)
		
		try:
			response = urlopen(request)
			html =  response.read()
			searchKey = '<div id="HeaderClubAddress">'
			start = html.find(searchKey)
			if start > 0:
				start += len(searchKey)
				stop = html.find('</div>', start)
				print start, stop
			
			
				addressHtml = html[start:stop].strip()
				print addressHtml
				addressHtml = addressHtml.replace('&nbsp', '').replace(';', '')
				addressArray = addressHtml.split('|')
#				print addressHtml
#				for idx, x in enumerate(addressArray):
#					print idx, x

				street = addressArray[0]

				addressHtml = addressArray[1]
				addressArray = addressHtml.split('<br />')
				phone = addressArray[1].strip()


				addressHtml = addressArray[0]
				addressArray = addressHtml.split(', ')
				city = addressArray[0].strip()

				addressHtml = addressArray[1]
				addressArray = addressHtml.split(' ')
				state = addressArray[0].strip()
				postalCode = addressArray[1].strip()
				

				print '=========='
				print street
				print city
				print state
				print postalCode
				print phone
				print '=========='

				try:
					conn.execute("INSERT INTO STORES(STORE_NUM, STREET, CITY, STATE, ZIPCODE, PHONE) VALUES(?,?,?,?,?,?)", (idx, street, city, state, postalCode, phone))

					conn.commit()
					print "Records created successfully"
				except sqlite3.IntegrityError:
					print "Not a unique store number"
			else:	
				print 'NOT FOUND'

		except URLError, e:
			print 'No kittez. Got an error code:', e

	store.getAll(conn)

if __name__ == '__main__':
	main()