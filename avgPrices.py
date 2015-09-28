class Product(object):
    def __init__(self):
        self.name = ''
        self.prices = []
        
    def averagePrice(self):
        total = sum(self.prices)
        return total / len(self.prices)        


def main():

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
        print 'Average price of {} is {}'.format(p.name, p.averagePrice())
    
    
if __name__ == "__main__":
    main()  