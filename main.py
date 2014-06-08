import itertools 
import yahoo

folder = 'historical'

def range_dict(dictionary, begin, end):
    return dict(itertools.islice(dictionary.iteritems(), begin, end+1))

def __saveQuotesIfNotExists(symbol, quotes):
    file = open("%s/%s_quotes.csv"%(folder,symbol),"w")
    file.write(quotes)
    file.close()

symbols = yahoo.getAllSymbols()
symbols = list(symbols)
tot = len(symbols)
print "starting saving historical data for %s symbols"%tot

#symbols = itertools.islice(symbols, 0, 100)
i = 1
for s in symbols:
    symbol = s['symbol']
    print "(%s/%s)saving historical data for %s"%(i,tot,symbol)
    quotes = yahoo.getHistoricalQuotesAsCSV(symbol)
    __saveQuotesIfNotExists(symbol, quotes) 
    i = i + 1

