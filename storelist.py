from urllib2 import Request, urlopen, URLError
import sqlite
def go():
    
    url='http://www3.samsclub.com/clublocator/club_detail.aspx?myclub={store_number}'

    for idx in range(1):
        #request store url
       store_url = (url.format(store_number=8209))
       request = Request(store_url)
       
       try:
            response = urlopen(request)
            html = response.read()
            searchKey = '<div id="HeaderClubAddress">'
            start = html(searchKey) + len(searchKey)
            stop = html.find('/div', start)
            print start, stop
           
           
            start = html.find('<div id="HeaderClubAddress">')
            if start > 0:
               addressHtml = html[start:stop].strip()
               addressHtml = addressHtml.replace('&nbsp', '').replace(';', '')
               addressArray = addressHtml.split('|')
               print addressHtml
               
               for idx, x in enumerate(addressArray):
                   print idx, x
                   
            street = addressArray[0]
    
            addressHtml = addressArray[1]
            addressHtml = addressHtml.split('<br />')
            phone = addressArray[1].strip()

            addressHtml = addressArray[0]
            addressArray = addressHtml.split(', ')
            city = addressArray[0].strip()

            addressHtml = addressArray[0]
            addressArray = addressHtml.split(', ')
            city = addressArray[0].strip()
    
            
            
            # city = addressArray[0]
#             phone = addressArray[1]
#             state = city.split(', ')[0].strip()
#             postalCode = city.split(', ')[1].strip()
#
            
            
            
            print '=========='
            print street
            print city
            print phone
            
            else:
                
                
            