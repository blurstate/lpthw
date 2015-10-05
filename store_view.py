import sqlite3

conn = sqlite3.connect('store.db')

cursor = conn.execute("SELECT STORE_NUMBER, ADDRESS from STORES")
for row in cursor:
	print "Store# =", row[0]
	print "Address =", row[1], "\n"
	
print "Op done successfully"

conn.close()