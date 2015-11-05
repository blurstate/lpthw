from urllib2 import Request, urlopen, URLError
import sqlite3
 #execution plan 
 #1) find a website (target.com)
# 2) find the store locator : http://gam.target.com/store-locator/sl/Fayetteville-Store/1470
 #3) learn ou URLs are strucred
# 4) loop from 1 to 10000, requestiong the store url 
# 5) pull the address info from the html
# 6) save to database


#using classses

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
            print "Street: ", row[1]
            print "City: ", row[2]
            print "State: ", row[3]
            print "ZIP: ", row[4]
            print "Phone: ", row[5], "\n"
            
        conn.close()




  


def go():

    #sqlite set ups
    conn = sqlite3.connect('samsclub.db')
    print "Opend database succesfully"
    
#    conn.execute('''CREATE TABLE STORES 
#        (STORE_NUM INT PRIMARY KEY NOT NULL,
#         STREET          TEXT        NOT NULL,
#         CITY            TEXT        NOT NULL,
#         STATE           TEXT        NOT NULL,
#         ZIP             INT         NOT NULL,
#         PHONE           INT         NOT NULL);''')
    
    print "created table seccesfully"    
        
        
# 2) find the store locator : http://gam.target.com/store-locator/sl/Fayetteville-Store/1470
    url='http://www3.samsclub.com/clublocator/club_detail.aspx?myClub={store_number}'
    
    # 4) loop through  1 to 10000 to find the different stores 
    for idx in range(4980,4987):
        # requesting the store url
        store_url=url.format(store_number=idx+1)
        request = Request(store_url)  #sets up the Request url
        print request
        print store_url
        
        try:
	        response = urlopen(request)  #opens URL
	        html = response.read()      #converets the responce into a read html string
	        # 5) pull the address info from the html
	        # 5.1 find the address
	        searchKey = '<div id="HeaderClubAddress">'  #key used with .find to find the info we need
	        
	        start= html.find(searchKey)
	        if start > 0 :
	            start += len(searchKey)
	            stop = html.find('</div>', start)   #key used to braket off the info
	            print start, stop
	        
	        
	            
	            addressHtml = html[start:stop].strip() #strip takes evertyhing out that is not between start:stop
	            addressHtml = addressHtml.replace( '&nbsp', '').replace(';','') #replaces text we dont need with nothing so that we have a cleaner string
	            addressArray = addressHtml.split('|') #uses | to split the html into a stacking array
	           # print ,addressHtml
	            
	           
	            print "=============="
	        
	           # for idx, x in enumerate(addressArray):    #used to see what info is in what spot of the array
	            #     print idx, x
	            
	            print"==============="
	            
	            street= addressArray[0]
	            
	            addressHtml= addressArray[1]
	            addressArray= addressHtml.split('<br />')        
	            phone = addressArray[1]                         #allocates the info from the array we built and sets it into the variables we want ie phon address and such
	            
	            addressHtml = addressArray[0]
	            addressArray= addressHtml.split(', ')
	            city = addressArray[0].strip()
	            
	            addressHtml = addressArray[1]
	            addressArray = addressHtml.split(' ')
	            state = addressArray[0].strip()
	            postalCode = addressArray[1].strip()
	            
	            
	            print "============"
	            print street 
	            print city
	            print state
	            print postalCode
	            print phone
	            print "============" 
	            
	            
	            #printing into sqlute
	            try:
	                conn.execute(" INSERT INTO STORES(STORE_NUM, STREET, CITY, STATE, ZIP, PHONE) VALUES(?,?,?,?,?,?)", (idx, street, city, state, postalCode, phone))   
	            
	                conn.commit()
	                print "records treated succesfully"       
	            except sqlite3.IntegrityError:
	                print"Not a unique data entry"
	        else:
	            print "NOT FOUND"

	       
	        
        except URLError, e:
            print 'No kittez. Got an error code:', e
    
    
    Store.getAll(conn)    
if __name__ == '__main__':
    go()
