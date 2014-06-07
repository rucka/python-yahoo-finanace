import itertools
import yahoo

def range_dict(dictionary, begin, end):
    return dict(itertools.islice(dictionary.iteritems(), begin, end+1))


symbols = yahoo.getAllSymbols()

for s in itertools.islice(symbols, 0, 10):
    print s

