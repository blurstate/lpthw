from urllib2 import Request, urlopen, URLError
import sqlite3

#    conn.execute('''CREATE TABLE STORES 
#        (store_num INT PRIMARY KEY NOT NULL,
#         street          TEXT        NOT NULL,
#         city            TEXT        NOT NULL,
#         state           TEXT        NOT NULL,
#         postal_code             INT         NOT NULL,
#         phone           INT         NOT NULL);''')

GREETING = 'Yo'

class Store(object):
    def __init__(self):
        self.number = -1
        self.street = ''
        self.city = ''
        self.state = ''
        self.postalCode = ''
        self.phone = ''
        
    def save(self):
        try:
            connection = sqlite3.connect('samsclub.db')
            cursor = connection.cursor
            sql = """
                insert into stores
                (store_num, street, city, state, zip, phone)
                values (?, ?, ?, ?, ?, ?);
            """
            connection.execute(sql, (self.number, self.street, self.city, self.state, self.postalCode, self.phone))
            connection.commit()
        except sqlite3.IntegrityError:
            print self.number, "already added"    
        
        connection.close
            
        
    @staticmethod
    def getAll(city=None):
        connection = sqlite3.connect('samsclub.db')
        cursor = connection.cursor
        params = []
        sql = """
            select * from stores
        """
        if city:
            sql += """
                where city = ?
            """
            params.append(city) 
        
        cursor = connection.execute(sql, params)
        
        stores = []
        for row in cursor:
            s = Store()
            s.number = row[0]
            s.street = row[1]
            s.city = row[2]
            s.state = row[3]
            s.postalCode = row[4]
            
            stores.append(s)
            
        connection.close()
        return stores

def go():
#    Execution plan
    # 3) learn how URLs are structured (http://gam.target.com/store-locator/sl/Alabaster-Store/<store number>
    url = 'http://www3.samsclub.com/clublocator/club_detail.aspx?myclub={store_number}'
    
    # 4) loop from 1 to 10000, 
    for idx in range(4968, 4975):
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
#                print 0, addressHtml
                    
                street = addressArray[0]
                
                addressHtml = addressArray[1]
#                print 1, addressHtml
                addressArray = addressHtml.split('<br />')
                phone = addressArray[1].strip()

                addressHtml = addressArray[0]
#                print 2, addressHtml
                addressArray = addressHtml.split(', ')
                city = addressArray[0].strip()
                
                addressHtml = addressArray[1]
#                print 3, addressHtml
                addressArray = addressHtml.split(' ')
                state = addressArray[0].strip()
                postalCode = addressArray[1].strip()
                      
                # print '========='
                # print street
                # print city
                # print state
                # print postalCode
                # print phone
                # print '========='
                
                s = Store()
                s.number = idx
                s.street = street
                s.city = city
                s.state = state
                s.postalCode = postalCode
                s.phone = phone
                s.save()
                
            else:
                print 'NOT FOUND'
                
        except URLError, e:
            print 'No kittez. Got an error code:', e   
            
    Store.getAll()
    

    # 6) save to database

if __name__ == '__main__':
    go()