from urllib2 import Request, urlopen, URLError
import sqlite3

class Store(object):
	def __init__(self):
		self.number = ''
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
			print "Street ", row[1]
			print "City ", row[2]
			print "State ", row[3]
			print "ZIP ", row[4]
			print "PHone ", row[5], "\n"
			
		conn.close()
		
		
		
		
	
	
	
	

def go():

	conn = sqlite3.connect('samsclub.db')
	print "Opened database succesfully"
	
	#conn.execute('''CREATE TABLE STORES
	#	(STORE_NUM INT PRIMARY KEY NOT NULL,
	#	STREET			TEXT		NOT NULL,
	#	CITY 			TEXT 		NOT NULL,
	#	STATE			TEXT		NOT NULL,
	#	ZIP				INT			NOT NULL,
	#	PHONE			INT			NOT NULL);''')
		
	#print "created table succesfully"

	
	url = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myclub={store_number}'
	
	for idx in range(4990,5000):
	
		store_url = url.format(store_number=idx+1)
		print store_url
		request = Request(store_url)
		try:
			response = urlopen(request)
			html = response.read()
			
			searchKey = '<div id="HeaderClubAddress">'
			start = html.find(searchKey) 
			if start > 0:
				start += len(searchKey)
				stop = html.find('<div>', start)
				print start, stop
				
			
				addressHtml = html[start:stop].strip()
				addressHtml = addressHtml.replace('&nbsp', '').replace(';','')
				addressArray = addressHtml.split('|')
				#print addressHtml
				#for idx, x in enumerate(addressArray):
				#	print idx, x
				
				street = addressArray[0]
				
				addressHtml = addressArray[1]
				#print 1, addressHtml
				addressArray = addressHtml.split('<br />')
				phone = addressArray[1].strip()
				
				
				addressHtml = addressArray[0]
				#print 2, addressHtml
				addressArray = addressHtml.split(', ')
				city = addressArray[0].strip()
				
				addressHtml = addressArray[1]
				#print 3, addressHtml
				addressArray = addressHtml.split(' ')
				state = addressArray[0].strip()
				postalCode = addressArray[1].strip()
				
				
				print '====='
				print street
				print city
				print state
				print postalCode
				print phone
				
				try:
					conn.execute("INSERT INTO STORES(STORE_NUM, STREET, CITY, STATE, ZIP, PHONE) VALUES(?,?,?,?,?,?)", (idx ,street, city, state, postalCode, phone))
					
					conn.commit()
					print "records created succesfully"
				except sqlite3.IntegrityError:
					print "Not a unique store number"
			else:
				print "Not found"
			
		except URLError, e:
			print 'No', e
	
	
	
	Store.getAll(conn)
	
if __name__ == '__main__':
	go()