from yahoo_finance import Share
from pprint import pprint

yahoo = Share('YHOO')

print(yahoo.get_open())
print(yahoo.get_trade_datetime())
print(yahoo.get_last_trade_with_time())


print(yahoo.get_historical('2017-03-03', '2017-03-07'))
#### the two dates specified above are "start date" and "end date". so you'll get all the historical data in btwn
#### returned data will be in dictionary format (more like JSON data format)

# use a more readable output format
pprint(yahoo.get_historical('2017-03-03', '2017-03-07'))

/Users/yisilala/PycharmProjects/stock/DataRetrievingYahoo.py