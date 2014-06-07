import urllib
import json
from xml.dom import minidom

urlbase = 'http://query.yahooapis.com/v1/public/yql?format={0}&q={1}&env=store://datatables.org/alltableswithkeys'

def getAllSymbols():
    #print('downloading data..')

    format = 'xml'
    query = 'select * from yahoo.finance.industry where id in (select industry.id from yahoo.finance.sectors)'
    url = urlbase.format(format, query) 
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

def __getMarket(symbol):
    if not symbol[-3:-2] == '.':
        return ''
    else:
        return symbol[-2:] 
