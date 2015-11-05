import web

#creating the urls
urls = (
  '/', 'index',
  '/stock', 'stock'
  #'/stock/(.+)', 'stock'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
	def GET(self):
		news = [
		{'label':'Man Walks on Mars!', 'url':'http://www.google.com'},
		{'label':'Big news in Programming!', 'url':'http://www.google.com'}
		]

		favorites = []

		return render.index(news=news, favorites=favorites)

class stock:
	def GET(self):
		stock_news=[
		{'label':'This Company is Awesome! -Mom', 'url':'http://www.google.com'},
		{'label':'Making money hand over fist.', 'url':'http://www.google.com'}
		]

		sec_filings=[
		{'label':'Google Filings', 'url':'http://www.nasdaq.com/symbol/goog/sec-filings'}
		]
		return render.stock(stock_news=stock_news, sec_filings=sec_filings)

if __name__ == '__main__':
    app.run()



