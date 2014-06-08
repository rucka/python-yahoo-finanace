import itertools
import urllib
import json
from xml.dom import minidom

'''
http://ichart.finance.yahoo.com/table.csv?s=INTC&a=06&b=9&c=1986&d=2&e=5&f=2008&g=d
s - This is where you can specify your stock quote, if you want to download stock quote for Microsoft, just enter it as 's=MSFT'
a - This parameter is to get the input for the start month. '00' is for January, '01' is for February and so on.
b - This parameter is to get the input for the start day, this one quite straight forward, '1' is for day one of the month, '2' is for second day of the month and so on.
c - This parameter is to get the input for the start year
d - This parameter is to get the input for end month, and again '00' is for January, '02' is for February and so on.
e - This parameter is to get the input for the end day
f - This parameter is to get the input for the end year
g - This parameter is to specify the interval of the data you want to download. 'd' is for daily, 'w' is for weekly and 'm' is for monthly prices. The default is 'daily' if you ignore this parameter.
'''

DATATABLES_URL = 'store://datatables.org/alltableswithkeys'
PUBLIC_API_URL = 'http://query.yahooapis.com/v1/public/yql?format={0}&q={1}&env=%s' %  DATATABLES_URL
HISTORICAL_URL = 'http://ichart.finance.yahoo.com/table.csv?s={0}'

def getAllSymbols():
    #print('downloading data..')

    format = 'xml'
    yql = 'select * from yahoo.finance.industry where id in (select industry.id from yahoo.finance.sectors)'
    url = PUBLIC_API_URL.format(format, yql) 
    #print (url)
    usock = urllib.urlopen(url)
    dataAsString = usock.read()
    dom = minidom.parseString(dataAsString)
    industries = dom.getElementsByTagName('industry')    
    for industry in industries:
        industryValue = industry.attributes['name'].value
        for company in industry.getElementsByTagName('company'):
            companyValue = company.attributes['name'].value
            symbolValue = company.attributes['symbol'].value
            marketValue = __getMarket(symbolValue)
            yield {'symbol': symbolValue,'market':marketValue, 'company': companyValue,'industry':industryValue}

def getHistoricalQuotesAsCSV(symbol):
    url = HISTORICAL_URL.format(symbol)
    #print(url)
    
    usock = urllib.urlopen(url)
    dataAsString = usock.read()
    lines = dataAsString.splitlines(True)
    header = 'symbol,%s'%lines[0]
    lines = ['%s,%s'%(symbol,line) for line in itertools.islice(lines, 1, None)] 
    
    dataAsString = __getCSV([header]+lines[::-1])
    return dataAsString

def __getCSV(results): 
    return ''.join(results)

def __getMarket(symbol):
    if not symbol[-3:-2] == '.':
        return ''
    else:
        return symbol[-2:] 

def __format_symbol_list(symbolList):
    return ",".join(["\""+stock+"\"" for stock in symbolList])

