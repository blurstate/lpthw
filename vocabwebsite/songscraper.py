#build classes for the artist lyric info to be scraped into 
#create url cycle that will go through all atist and scrpe the site 
# make sure that scraper will first make a list of each artist. then of there songs to fill he html. 


from urllib2 import Request, urlopen, URLError
import sqlite3
from time import sleep



class Artist(object):
	def __init__(self):
		self.name=''
		self.album=[]
		self.url=""
	
	artistId=0
	
class Album(object):
	def __init__(self):
		self.name=''
		self.songs=[]
		self.artistId=0
		self.year="N/A"
	
	
class Song(object):
	def __init__(self):
		self.name=''
		self.text=''
		self.songurl=''
		self.artistId=0
	
	

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
from songhtml import songstring

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
				#ask=raw_input("Is this the right artist? (Y)yes or (N)no: ")
				ask='y'
				if (ask.lower()=='y'):
					a=Artist()
					
					
					a.name=artistName
					a.url=artistUrl

					x+=1

						
						
						
						
						
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
			
			#print album.name
			#print album.year
			
			#a.album.append(album)
			
			songList=i.split("<a")
			count=0
			singlesList=[]
			singlesMark=False

			for i in songList:

				if (i[0:9]==' href="..'):
					if (singlesMark==True):			# strips the song name and url from html
						#find name
						song=Song()
						start=i.find(">")
						start+=len(">")
						stop=i.find("</a>",start)
						song.name=i[start:stop].strip()
						#find url
						start=i.find('"..')
						start+=len('"..>')
						stop=i.find('" t',start)
						song.songurl=i[start:stop].strip()
						#append
						singlesList.append(song)





					elif (singlesMark==False):		#strips the song name and url from html and appends to the album class list
						#find name
						song=Song()
						start=i.find(">")
						start+=len(">")
						stop=i.find("</a>",start)
						song.name=i[start:stop].strip()
						#find url
						start=i.find('"..')
						start+=len('"..>')
						stop=i.find('" t',start)
						song.songurl=i[start:stop].strip()
						#append
						album.songs.append(song)

				if (i[162:199]=='<div class="album">other songs:</div>'):
					print '=======other songs ======'
					singlesMark=True

			print"===========appending songs==========================="

			# if singlesMark==True:
			# 	album.name="Single Tracks"
			# 	for i in singlesList:
			# 		album.songs.append(i.name)
			# 		#print i.name
			# 	a.album.append(album)
			a.album.append(album)
			if singlesMark==True:
				singleAlbum=Album()
				singleAlbum.name="Single Tracks"
				for i in singlesList:
					singleAlbum.songs.append(i)
				a.album.append(singleAlbum)



	except URLError, e:
			print "Found and Error code:", e

	for i in a.album[1:2]:
		print"====================="
		print i.name
		print i.year
		print"=====================","====================="
		for x in i.songs[0:1]:
			print x.name
			print "url code ==", x.songurl
			try:
				# url="http://www.azlyrics.com/{}".format(x.songurl)
				# request=Request(url)
				# responce=urlopen(request)
				# songhtml=responce.read()
				lyrics=songstring
			except URLError, e:
				print "Found an Error Code:", e

			start=lyrics.find("that. -->")
			start+=len("that. -->")
			stop=lyrics.find("<!--",start)
			print start, stop
			lyrics=lyrics[start:stop].strip()
			x.text=lyrics
			print x.text







artistSearch("Led Zeppelin")


#findArtists()
	