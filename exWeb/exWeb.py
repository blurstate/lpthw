import web
import storelists
import sqlite3
urls = (
'/', 'index',
'/hogs','razorback',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class razorback:
	def GET(self):
		html= """
			<html>
				<head></head>
				<body>
					<h1>Beat Bama!!!</h1>
					
				</body>
			</html>
		"""
		return html

class index(object):
	def GET(self):
		conn = sqlite3.connect('samsclub.db')
		stores = storelists.Store.getAll(conn)			
		return render.index(Stores = stores)

	
if __name__== '__main__':
		
	
	app.run()
			