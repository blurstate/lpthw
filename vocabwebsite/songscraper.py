#build classes for the artist lyric info to be scraped into 
#create url cycle that will go through all atist and scrpe the site 
# make sure that scraper will first make a list of each artist. then of there songs to fill he html. 


from urllib2 import Request, urlopen, URLError
import sqlite3
from time import sleep


class Artist():
	name=''
	album=[]
	url=""
	
	artistId=0
	
class Album():
	name=''
	song=[]
	artistId=0
	
	
class Song():
	name=''
	text=''
	artistId=0
	
	

def findArtists():
	dataBase=[]
	
	
	idnum=0
	
	for a in range(97,98):
		
		sleep(60)
		url="http://www.azlyrics.com/{}.html" .format(chr(a))
		request=Request(url)

		try:
			responce=urlopen(request)
			html=responce.read()

			searchKey='<!-- main -->'
			start= html.find(searchKey)
			if start > 0:
				start += len(searchKey)
				stop = html.find('<!-- container main-page -->', start)  

				artistString=html[start:stop].strip()
				artistList=artistString.split('<a ')
				for i in artistList:
					end=0
					if (i.startswith("href")==True):
						end+=1

						idnum+=1
						artist=Artist()			#assings the artists name url, and id then will append to a list 
						artist.artistId=idnum


						start=i.find('href="')
						start+= len('href="')
						stop=i.find('">',start)
						artist.url=i[start:stop].strip()  # sets artist url key
						#print artist.url

						start=i.find('">')
						start+= len('">')
						stop=i.find('</a>')
						artist.name=i[start:stop].strip() #sets artist name\
						#print artist.name

						dataBase.append(artist)
						if end==5:
							break
				for i in dataBase:
					print i.name
					print i.artistId
					print i.url
					print "==========="
 

		except URLError, e:
				print "Found and Error code:", e
from searchhtml import text

def artistSearch(name):

	name=name.replace(" ","+")
	url="http://search.azlyrics.com/search.php?q={}" .format(name)
	# request=Request(url)

	try:
			# responce=urlopen(request)
			# html=responce.read()
			html=text
			# print html
			searchKey='1. <a'
			start= html.find(searchKey)
			if start > 0:
				start += len(searchKey)
				stop = html.find('</a>', start)

				html=html[start:stop].strip()


				# artistList=artistString.split('<a ')



	except URLError, e:
			print "Found and Error code:", e





artistSearch("Led Zeppelin")

# findArtists()
	