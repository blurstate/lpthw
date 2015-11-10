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
	year=0
	
	
class Song():
	name=''
	text=''
	artistId=0
	
	

artistData=[]					#will appened into these list to hold songs albums and such. will use artistId to organize for the data 
albumData=[]
songData=[]
	
def findArtists():
	dataBase=[]
	
	


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
from artisthtml import artisttext

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
			artistUrl=html[len('href="'):html.find('" target',len('href="'))].strip()
				
			start=html.find('<b>')
			start+=len('<b>')
			artistName=html[start:html.find('</b>',len('<b>'))].strip()
			
			print"The artist name is "
			print artistName
			print artistUrl
			
			x=0
			while(x==0):
				ask=raw_input("Is this the right artist? (Y)yes or (N)no: ")
				if (ask.lower()=='y'):
					a=Artist()
					
					
					a.name=artistName
					a.url=artistUrl
					x+=1
					#return(a)
						
						
						
						
						
				elif (ask.lower()=='n'):
					print "please search a new artist"
					x+=1
				else:
					print"Please enter (Y) or (N)"
						
	
	except URLError, e:
			print "Found and Error code:", e
			
	url=a.url
	#request=Request(url)
	
	
	try:						#this step takes the album and song list url and fills the classes so that the artist class will have a list of albums and each album will have a list of songs with a url for each lyric page 
		
		
		#responce=urlopen(request)
		#html=responce.read()
		html=artisttext
		
		key="<!-- start of song list -->"
		start=html.find(key)
		start+=len(key)
		stop=html.find('<script type="text/javascript">',start)
		html=html[start:stop].strip()
		albumList=html.split("<a id=")
		
		for i in albumList:
			print"============================"
			album=Album()
			start=i.find('<b>"')
			start+=len('<b>"')				#pulls album name
			stop=i.find('"</b>',start)
			album.name=i[start:stop].strip()
			
			start=i.find('(')
			start+=len('(')
			stop=i.find(')',start)
			album.year=i[start:stop].strip()
			
			print album.name
			print album.year
			
			a.album.append(album)
			
			songList=i.split("<a")
			count=0
			for i in songList:
				if (i[0:9]==' href="..'):
					song=Song()
					start=i.find(">")
					start+=len(">")
					stop=i.find("</a>",start)
					song.name=i[start:stop].strip()
					print song.name
							
			print"==========================="		
		


	except URLError, e:
			print "Found and Error code:", e





artistSearch("Led Zeppelin")
#print a.name, a.url

#findArtists()
	