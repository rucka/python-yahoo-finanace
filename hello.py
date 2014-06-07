import urllib
import json
#https://code.google.com/p/pyql/source/browse/source/pyql.py?r=e8e1ecaa1be1e655acd679707c0d9080b779a071
#https://github.com/gurch101/StockScraper/blob/master/stockretriever.py
print('downloading data..')

url = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.industry%20where%20id%20in%20(select%20industry.id%20from%20yahoo.finance.sectors)'#&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
urlbase = 'http://query.yahooapis.com/v1/public/yql?format=json&q={0}&env=store://datatables.org/alltableswithkeys'
query = 'select * from yahoo.finance.industry where id in (select industry.id from yahoo.finance.sectors)'
url = urlbase.format(query) 
print (url)
u = urllib.urlopen(url)





#data = u.read()
data = json.loads(u.read())
print(data)
