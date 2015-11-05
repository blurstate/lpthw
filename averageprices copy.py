def do_average(prices):
    total = 0
    
    for p in prices:
        total = total + p
    
    return total / len(prices)
    
proucts = {}

producs['gum'] = [.25, .5, .35]
products['soda'] = [1.25, 2.5]

for name, prices in products.iteritems():
    avg = do_average(prices)
    print''