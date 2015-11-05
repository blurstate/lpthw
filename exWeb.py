import web

urls = (
'/', 'index',
'/hogs','razorback',
)

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

class index:
	def GET(self):
		html= """
			<html>
				<head></head>
				<body>
					<h1>Hello World</h1>
					
				</body>
			</html>
		"""
		
		return html

	
if __name__== '__main__':
		
	app = web.application(urls, globals())
	app.run()
			