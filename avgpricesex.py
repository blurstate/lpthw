class Product(object):
    def __init__(self):
        self.name = ''
        self.prices = []
        
    def averagePrice(self):
        return doAverage(self.prices)      


def doAverage(prices):
    total = sum(prices)
    return total / len(prices)
    

def print_blank_lines(num_lines):
    for i in range(0,num_lines):
        print ''

def main():

    print_blank_lines(1)

    
    # Dictionary
    products = {}
    products['chips'] = [2,3,4,5]
    products['bread'] = [3,4,5,6]
    products['candy'] = [4,5,6,7]
    
    for name, prices in products.iteritems():
        avg = doAverage(prices)
        print 'DICTIONARY: Average price of {} is {}'.format(name, avg)


    print_blank_lines(2)
    
    # Class
    products = []

    p = Product()
    p.name = 'Gum'
    p.prices = [1,2,3,4,5]
    products.append(p)

    p = Product()
    p.name = 'Soda'
    p.prices = [6,7,8,9]
    products.append(p)

    for p in products:
        print 'CLASS and LIST: Average price of {} is {}'.format(p.name, p.averagePrice())
        
    print_blank_lines(1)
    
if __name__ == "__main__":
    main()  