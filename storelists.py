from urllib2 import Request, urlopen, URLError
import sqlite3



GREETING = 'Yo'

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
                    print "Phone ", row[5], "\n"
            
            conn.close()


def go():
    
        conn = sqlite3.connect('samsclub.db')
        print "Opened database succesfully"
    
    conn.execute(''' Create table stores (STORE_NUM int primary key not null ,STREET TEXT NOT NULL, CITY TEXT NOT NULL, STATE TEXT NOT NULL, ZIP TEXT NOT NULL, PHONE TEXT NOT NULL); ''')

#    Execution plan
    # 3) learn how URLs are structured (http://gam.target.com/store-locator/sl/Alabaster-Store/<store number>
        url = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myclub={store_number}'
    
    # 4) loop from 1 to 10000, 
        for idx in range(4975, 4990):
        # requesting the store url
                store_url = url.format(store_number=idx+1)
                print store_url
                request = Request(store_url)
                try:
                        response = urlopen(request)
            
            # 5) pull the address info from the html
            # 5.1 find the address
            # - find a div that contains the data
            # - slice the html starting at that div until the end of that div
            
            
                        html = response.read()
                        searchKey = '<div id="HeaderClubAddress">'
                        start = html.find(searchKey)
                        if start > 0:
                                start += len(searchKey)
                                stop = html.find('</div>', start)
                                print start, stop
                
                
                                addressHtml = html[start:stop].strip()
                                print addressHtml
                                addressHtml = addressHtml.replace('&nbsp', '').replace(';','')
                                addressArray = addressHtml.split('|')
                                #print 0, addressHtml
                                # for idx, x in enumerate(addressArray):
                                #     print idx, x
                    
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
                
                
                                print '========='
                                print street
                                print city
                                print state
                                print postalCode
                                print phone
                                print '========='
                
                                try:
                                        conn.execute("INSERT INTO STORES(STORE_NUM, STREET, CITY, STATE, ZIP, PHONE) VALUES(?,?,?,?,?,?)", (idx, street, city, state, postalCode, phone))
                
                                        conn.commit()
                                        print "records created succesfully"
                                except sqlite3.IntegrityError:
                                        print "Not a unique store number"
                    
            
                        else:
                                print 'NOT FOUND'
                
                except URLError, e:
                        print 'No kittez. Got an error code:', e   
    
        Store.getAll(conn)

    # 6) save to database

if __name__ == '__main__':
        go()