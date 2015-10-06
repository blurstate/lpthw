from urllib2 import Request, urlopen, URLError
import sqlite3

class Store():
	def __init__(self):
		self.number =''
		self.street = ''
		self.city = ''
		self.state = ''
		self.postalCode = ''
		self.phone = ''
	@staticmethod
	def getAll(connect):
		c=connect.cursor()
		c.execute('''SELECT * from stores''')
		for row in c:
			print'Store Number: {} is at {}, {}, {} {} and the phone number is {}.'.format(row[0],row[1],row[2],row[3],row[4],row[5])
	

def main():
	
	url = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myclub={store_number}'
	storeBeg = 4968

	conn = sqlite3.connect(":memory")
	print 'Opened database successfully'
	conn.execute('''DROP TABLE stores;''')
	conn.execute('''CREATE TABLE STORES (number primary key not null, address not null, city not null, state not null, zipcode not null, phone not null);''')


	for idx in range(storeBeg,storeBeg+5):
		
		storeUrl = url.format(store_number=idx)
		print storeUrl
		request = Request(storeUrl)
		try:
			response = urlopen(request)
			html = response.read()
			searchKey = '<div id="HeaderClubAddress">'			#print html
			start = html.find(searchKey)
			end = html.find('</div>',start)
#			print start, end
			#print html[start:end].strip()
			if start >0:
				start +=  + len(searchKey)
				addressHtml = html[start:end].strip()
				addressHtml = addressHtml.replace('&nbsp','').replace(';','')
				addressArray = addressHtml.split('|')
#				print 0, addressHtml
				#for idx, x in enumerate(addressArray):
				#	print idx, x
				
				street = addressArray[0]

				addressHtml = addressArray[1]
#				print 1, addressHtml
				addressArray = addressHtml.split('<br />')
				
				addressHtml = addressArray[0]
				phone = addressArray[1].strip()
#				print 2, addressHtml
				addressArray = addressHtml.split(', ')
				city = addressArray[0]
				
				addressHtml = addressArray[1]
#				print 3, addressHtml
				addressArray = addressHtml.split(' ')
				state = addressArray[0].strip()
				postalCode = addressArray[1].strip()

				#print '____'
				# print 'Store Number = {}'.format(idx)
				# print street
				# print city
				# print state
				# print postalCode
				# print phone
				# print '_____'

				try:
					conn.execute('''INSERT INTO stores(number, address, city, state, zipcode, phone) values(?,?,?,?,?,?);''', (idx,street, city, state, postalCode,phone))
					conn.commit()
				except sqlite3.IntegrityError:
						print "Not a unique store number."
		except URLError, e:
			print 'error'
	print '-----------------------'		
	Store.getAll(conn)				

if __name__=='__main__':
	main()