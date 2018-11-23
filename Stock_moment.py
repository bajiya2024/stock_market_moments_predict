from pandas_datareader import data as pdr
import fix_yahoo_finance as yffrom matplotlib import pyplot as plt
import pandas as pd
import numpy as np

import datetime
print(pd.__version__)
print(np.__version__)
companies_dict={
    'Amazone':'AMZN',
    'Apple':'AAPL',
    'Walgreen':'WBA',
    'Northrop':'NOC',
    'Boing':'BA',
    'Lockheed Martin':'LMT',
    'McDonalds':'MCD',
    'Intel':'INTC',
    'Navistar':'NAV',
    'IBM':'IBM',
    'Texas Instruments':'IXN',
    'MasterCard':'MA',
    'Microsoft':'MSFT',
    'General Electrices':'GE',
    'Symantec':'SYMC',
    'American Express':'AXP',
    'Pepsi':'PEP',
    'Coca Cola':'KO',
    'Jonhson & johnson':'JNJ',
    'Toyota':'TM',
    'Honda':'HMC',
    'Mistubishi':'MSBHY',
    'Sony':'SNE',
    'Exxon':'XOM',
    'Chevron':'CVX',
    'Valero Energy':'VLO',
    'Ford':'F',
    'State Bank Of india':'SBI'
}
 companies = sorted(companies_dict.items(),  key=lambda x: x[1])
print (companies)
#Define which online source to use 
#data_source ="yahoo"
#company_list = ['AMZN','AAPL','WBA']
#define the strat and end date
start_date = '2015-06-06'
end_date = '2016-06-06'
#using pandas_datareader to load the desired stock data
#panel_data = data.DataReader(list(companies_dict.values()),data_source, start_date, end_date)
# download dataframe
yf.pdr_override()
data = pdr.get_data_yahoo(companies_dict.values(), start="2012-01-01", end="2013-04-30")
#stocks = pdr.get_data_yahoo("SPY", start_date, end_date)


#print the axiis panel 
print(data.axes)

#find stack close and open data values
Close_Stocks = data['Close']
Open_Stcoks = data['Open']
print "Closing stocks for different comapnies \n" ,stocks.iloc[0]
print "Opening stocks for different comapnies \n" ,stocks.iloc[0]


#calculationg daily stack moments 
stack_close = np.array(Close_Stocks).T
stack_open = np.array(Open_Stcoks).T
print stack_close

#find out the rows and columns
row, col = stack_close.shape
print (row)
print (col)
movements = np.zeros([row, col])
#print movements
for i in range(0, row):
    movements[i,:]= np.subtract(stack_close[i,:], stack_open[i,:])
#print movements
    print((movements[i][:]))

	
for i in range (0, len(companies)):
    print("companny:{}, changes: {}".format(companies[i][0], sum(movements[i][:])))
	
movements.shape
