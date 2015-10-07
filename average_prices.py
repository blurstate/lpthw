##AVERAGE PRICES#

#-- make a function
# - its job will be to find the average in a list of numbers
# - it should accept two params
#   - product_name
#   - prices
# - it should print "Finding average price for <prouct name>"
# - it should return the average price to the main program#

#- main program should loop through a dictionary of product names and prices, 
#    calling this function and printing the name and average as it goes#

prices = {
    'gum': [.25, .45, 1.50],
    'milk': [3.25, 4.75, 5.00],
    'bread': [1.76, 2.34, 1.98, 2.86],
    'eggs': [1.78, 2.30, 3.88]
}

#*** bonus, do it with a class instead ***




def average(product_name, prices):
	sum = 0
	print "Finding average price for %s" % product_name
	for price in prices:
		sum = sum + price
	return sum / len(prices)


for product_name, product_prices in prices.items():
	print average(product_name, product_prices)






class average_prices(object):
	"""docstring for average_prices"""
	def __init__(self):
		self.name = ''
		self.prices = []
		
products = []

p = Product()
p.name = 'Gum'
p.prices = [1,2,3,4,5]
products.append(p)

p = Product()
p.name = 'Soda'
p.prices = [1,2,3,4,5,6,7]
products.append(p)