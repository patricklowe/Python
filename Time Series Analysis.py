#!/usr/bin/env python
# coding: utf-8

# ##### Stock Analysis - Patrick Lowe, 16725829
# In this assignment I will be looking at 3 stock markets; Activision Blizzard (ATVI), Electronic Arts (EA), and Nintendo(NTDOY). I have a personal interest in these games but felt that choosing 3 from similair industries will allow for better insight into trends such as large declines or inclines. I may also use the odd 4th stock market as trend comparison to see if the trend is industry specific. Using various charts I will try to create the following:
# - Display stock on daily, monthly, and annual frequences
# - Identify trends by company/industry
# - Identify if day of the week influences investment
# 
# These datasets can be viewed here:
# Activision Blizzard - http://mlg.ucd.ie/modules/COMP30760/stocks/atvi.html
# Electronic Arts - http://mlg.ucd.ie/modules/COMP30760/stocks/ea.html
# Nintendo - http://mlg.ucd.ie/modules/COMP30760/stocks/ntdoy.html

# Firstly, we will import the relevant packages necessary for processing and analysing these markets.

# In[1]:


import pandas as pd
import datetime
import calendar
import os.path
import matplotlib
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import csv
import matplotlib.pylab as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Beautiful Soup is fantastic tool I've used in previous personal projects as a HTML parser, I'll be using this as a way of downloading and processing the data, which I will then store in a CSV file. Storing it in a the CSV is not required but I felt it was easier to work with.

# In[2]:


#   Specify the URL for Activision Blizzard, Electronic Arts, and Nintendo respectively
ATVI =   "http://mlg.ucd.ie/modules/COMP30760/stocks/atvi.html"
EA =   "http://mlg.ucd.ie/modules/COMP30760/stocks/ea.html"
NTDOY = "http://mlg.ucd.ie/modules/COMP30760/stocks/ntdoy.html"

#   Query the website and return the html to the variable "page"
ATVI_Page = urllib.request.urlopen(ATVI)
EA_Page = urllib.request.urlopen(EA)
NTDOY_Page = urllib.request.urlopen(NTDOY)

#   Parse the HTML using Beautiful Soup and store in variable "Soup"
ATVI_Soup = BeautifulSoup(ATVI_Page,"html.parser")
EA_Soup = BeautifulSoup(EA_Page,"html.parser")
NTDOY_Soup = BeautifulSoup(NTDOY_Page,"html.parser")

#   Print sample results
print(ATVI_Soup)


# ## Creating Dataframe Headers
# Here we are creating headers for the new dataframe, for each of the 3 stocks. I have commented out the 1st 4, I wanted to show that it's possible to get header by header from the HTML parser, but I decided to amalgamate the dates into a new header "Date", which we will also be transforming into the row index later. I also added an additional header, "Day" which will store the day of the week.

# In[3]:


ATVI_Head = ATVI_Soup.find("thead")
for result in ATVI_Head:
    headerData = result.find_all("td")
#    H1 = headerData[0].text # Stock
#    H2 = headerData[1].text # Year
#    H3 = headerData[2].text # Month
#    H4 = headerData[3].text # Day
    H5 = headerData[4].text # Open
    H6 = headerData[5].text # High
    H7 = headerData[6].text # Low
    H8 = headerData[7].text # Close

#   Create and write headers to a list 
ATVI_Rows = []
ATVI_Rows.append(["Date",H5,H6,H7,H8,"Day"])

print(ATVI_Rows)


# In[4]:


EA_Head = EA_Soup.find("thead")
for result in EA_Head:
    headerData = result.find_all("td")
#    H1 = headerData[0].text # Stock
#    H2 = headerData[1].text # Year
#    H3 = headerData[2].text # Month
#    H4 = headerData[3].text # Day
    H5 = headerData[4].text # Open
    H6 = headerData[5].text # High
    H7 = headerData[6].text # Low
    H8 = headerData[7].text # Close

#   Create and write headers to a list 
EA_Rows = []
EA_Rows.append(["Date",H5,H6,H7,H8,"Day"])


# In[5]:


NTDOY_Head = NTDOY_Soup.find("thead")
for result in NTDOY_Head:
    headerData = result.find_all("td")
#    H1 = headerData[0].text # Stock
#    H2 = headerData[1].text # Year
#    H3 = headerData[2].text # Month
#    H4 = headerData[3].text # Day
    H5 = headerData[4].text # Open
    H6 = headerData[5].text # High
    H7 = headerData[6].text # Low
    H8 = headerData[7].text # Close

#   Create and write headers to a list 
NTDOY_Rows = []
NTDOY_Rows.append(["Date",H5,H6,H7,H8,"Day"])


# ## Loading stock into our Dataframes
# Here we are using the HTML parser to load specific data into our dataframes. As above, we are gathering all column data into R1 through R8 and R9 holds our new amalgamated date (year-month-day), and the final entry into each row is the day of the week that stock was marked. The if statement will check if the current 'result' is actually a table heading for a new stock year and prevent that data from entering our dataset.

# In[6]:


ATVI_Table = ATVI_Soup.find("div", attrs={"class": "container"})
ATVI_Results = ATVI_Table.find_all("tr")
for result in ATVI_Results:
    stockData = result.find_all("td")
    R1 = stockData[0].text  # Stock Name
    R2 = stockData[1].text  # Year
    R3 = stockData[2].text  # Month
    R4 = stockData[3].text  # Day
    R5 = stockData[4].text  # Open
    R6 = stockData[5].text  # High
    R7 = stockData[6].text  # Low
    R8 = stockData[7].text  # Close
    R9 = stockData[1].text + "-" + stockData[2].text + "-" + stockData[3].text
    if stockData[0].text == "Stock":
        continue
    y = int(stockData[1].text);
    m = int(stockData[2].text);
    d = int(stockData[3].text);
    this_date = datetime.datetime(y,m,d)
    this_day = (calendar.day_name[this_date.weekday()])
    ATVI_Rows.append([R9,R5,R6,R7,R8,this_day])
print(ATVI_Rows)


# In[7]:


EA_Table = EA_Soup.find("div", attrs={"class": "container"})
EA_Results = EA_Table.find_all("tr")
for result in EA_Results:
    stockData = result.find_all("td")
    R1 = stockData[0].text  # Stock Name
    R2 = stockData[1].text  # Year
    R3 = stockData[2].text  # Month
    R4 = stockData[3].text  # Day
    R5 = stockData[4].text  # Open
    R6 = stockData[5].text  # High
    R7 = stockData[6].text  # Low
    R8 = stockData[7].text  # Close
    R9 = stockData[1].text + "-" + stockData[2].text + "-" + stockData[3].text
    if stockData[0].text == "Stock":
        continue
    y = int(stockData[1].text);
    m = int(stockData[2].text);
    d = int(stockData[3].text);
    this_date = datetime.datetime(y,m,d)
    this_day = (calendar.day_name[this_date.weekday()])
    EA_Rows.append([R9,R5,R6,R7,R8,this_day])


# In[8]:


NTDOY_Table = NTDOY_Soup.find("div", attrs={"class": "container"})
NTDOY_Results = NTDOY_Table.find_all("tr")
for result in NTDOY_Results:
    stockData = result.find_all("td")
    R1 = stockData[0].text  # Stock Name
    R2 = stockData[1].text  # Year
    R3 = stockData[2].text  # Month
    R4 = stockData[3].text  # Day
    R5 = stockData[4].text  # Open
    R6 = stockData[5].text  # High
    R7 = stockData[6].text  # Low
    R8 = stockData[7].text  # Close
    R9 = stockData[1].text + "-" + stockData[2].text + "-" + stockData[3].text
    if stockData[0].text == "Stock":
        continue
    y = int(stockData[1].text);
    m = int(stockData[2].text);
    d = int(stockData[3].text);
    this_date = datetime.datetime(y,m,d)
    this_day = (calendar.day_name[this_date.weekday()])
    NTDOY_Rows.append([R9,R5,R6,R7,R8,this_day])


# ## Export Dataset to CSV, Import to Dataframe
# This step is not necessary, we could continue to process the data by loading it into a dataframe from the rows above, but I felt that working with CSV files made for quicker editing on my part. Below, we are exporting the 3 stocks to their own CSV file respectively. Then we will check that the file has written successfully and load the data back into a dataframe with its respective name.

# In[9]:


with open('Blizzard_Stock.csv','w', encoding="utf-8",newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(ATVI_Rows)


# In[10]:


with open('EA_Stock.csv','w', encoding="utf-8",newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(EA_Rows)


# In[11]:


with open('Nintendo_Stock.csv','w', encoding="utf-8",newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(NTDOY_Rows)


# In[12]:


if not os.path.exists( "Blizzard_Stock.csv" ):
    print("Missing dataset file - Blizzard_Stock.csv")
else:
    print("Loaded Activison Blizzard Stock File")
    
if not os.path.exists( "EA_Stock.csv" ):
    print("Missing dataset file - EA_Stock.csv")
else:
    print("Loaded Electronic Arts Stock File")
    
if not os.path.exists( "Nintendo_Stock.csv" ):
    print("Missing dataset file - Nintendo_Stock.csv")
else:
    print("Loaded Nintendo Stock File")


# In[13]:


# Import CSV files as dataframes
df_ATVI = pd.read_csv("Blizzard_Stock.csv")
df_EA = pd.read_csv("EA_Stock.csv")
df_NTDOY = pd.read_csv("Nintendo_Stock.csv")

# View a Sample
df_ATVI.head(5)


# The next step is to handle any missing data entries appropriately. I managed to find a link (below) that allows us to view data for any given period, it would be possible to then use this table to replace the missing data with absolutely valid data but was too labour intensive for this assignment. Instead, I have opted for the second best solution, in my opinion. We will store the last known (i.e. previous) data entry for the missing data. Secondly, we are going to change the index of the rows to the date column, and also transform it to date/time type for better processing within graphs.
# 
# https://investor.activision.com/stock-information/historic-stock-lookup?8c7bdd83-a726-4a84-b969-494be2477e47%5BATVI_O%5D%5Bdate_month%5D=02&8c7bdd83-a726-4a84-b969-494be2477e47%5BATVI_O%5D%5Bdate_day%5D=1&8c7bdd83-a726-4a84-b969-494be2477e47%5BATVI_O%5D%5Bdate_year%5D=2012
# 

# In[14]:


# Replace missing data with forward fill
df_ATVI.fillna(method='ffill', inplace=True)
df_EA.fillna(method='ffill', inplace=True)
df_NTDOY.fillna(method='ffill', inplace=True)

# Update row index to relevant date, change index type to datetime
df_ATVI.index = pd.to_datetime(df_ATVI['Date'])
##df_ATVI = df_ATVI.drop(['Date'], axis=1)

df_EA.index = pd.to_datetime(df_EA['Date'])
##df_EA = df_EA.drop(['Date'], axis=1)

df_NTDOY.index = pd.to_datetime(df_NTDOY['Date'])
##df_NTDOY = df_NTDOY.drop(['Date'], axis=1)


# ## Daily Frequencies
# Now lets start viewing our data, firstly we will look at daily frequencies across the 7 year range by creating a new dataframe called df_STOCKNAME_Daily, this is not really necessary as the data is already in daily format, but I have opted to do this for consistency.

# In[15]:


# Daily Stock
Stocks = ["ATVI","EA","NTDOY"]
for stock in Stocks:
    exec("df_{}_Daily = df_{}.resample('D').mean()".format(stock,stock))


# In[16]:


plt.figure(figsize=(20,10))
for stock in Stocks:
    exec("plt.plot(df_{}_Daily['Close'],marker='o', label='{}',markersize=3, linewidth=2)".format(stock,stock))
plt.title("Activision Blizzard Stock, Daily Mean")
plt.legend(loc=3, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# What should be obvious is the 3 companies being fairly tied around 2012, but halfway through 2013 they start to diverge. Lets scale up the 2013 - 2014 period for these 3 and try narrow down a timeframe for the growth of EA.

# In[17]:


for stock in Stocks:
    exec("df_{}_2013 = df_{}[df_{}['Date'].str.contains('2013')].copy()".format(stock,stock,stock))
    
plt.figure(figsize=(20,10))
for stock in Stocks:
    exec("plt.plot(df_{}_2013['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)".format(stock,stock))
plt.title("Stock Market, 2013")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# We can see that EA took a jump in early May 2013. From research this correlates to EA acquiring the exclusive right to the Star Wars games. We can also see a jump for Activision Blizzard in February 2013, this appears to be from their parent company Vivendi selling their shares.
# 
# EA, May - https://ie.ign.com/articles/2013/05/10/ea-sports-executive-vice-president-sells-all-stock
# 
# ATVI, Feb - https://seekingalpha.com/article/1603122-sell-the-news-on-activision-blizzard

# ## Monthly Frequencies
# Next we will look at a slightly larger scale of the market, this should show us larger changes in the stock market. We can achieve this by creating a new dataframe for the monthly mean of each stock and plotting the 7 year range. Let's start large by looking at Quartly means.

# In[18]:


# Quarterly
for stock in Stocks:
    exec("df_{}_Quarterly = df_{}.resample('Q').mean()".format(stock,stock))


# In[19]:


plt.figure(figsize=(20,10))
for stock in Stocks:
    exec("plt.plot(df_{}_Quarterly['Close'],marker='o', label='{}',mec='white',markersize=9, linewidth=2)".format(stock,stock))
plt.title("Quartly Stock Mean")
plt.legend(loc=2, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# From the larger scale graph we cannot clearly see the jump in 2013 for both Electronic Arts (around May), or Activision Blizzard (around February). We can however see more prominant changes like a steeper than average increase for all 3 companies in 2015 - 2016. Lets look at this in a slightly smaller scale, monthly.

# In[20]:


# Monthly
for stock in Stocks:
    exec("df_{}_Monthly = df_{}.resample('M').mean()".format(stock,stock))


# In[21]:


plt.figure(figsize=(20,10))
for stock in Stocks:
    exec("plt.plot(df_{}_Monthly['Close'],marker='o', label='{}',mec='white',markersize=9, linewidth=2)".format(stock,stock))
plt.title("Monthly Stock Mean")
plt.legend(loc=2, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# We can get a clearer picture on which months caused the stock jump, for EA it appears Feb/March, for ATVI its a steady increase from about June to December before dropping in Jan/Feb 2016, and NTDOY takes increase in March/April/May 2015. Lets scale this down even further to see what could cause this.

# In[22]:


for stock in Stocks:
    exec("df_{}_2015 = df_{}[df_{}['Date'].str.contains('2015')].copy()".format(stock,stock,stock))
    
plt.figure(figsize=(20,10))
for stock in Stocks:
    exec("plt.plot(df_{}_2015['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)".format(stock,stock))
plt.title("Stock Market, 2015")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# We've narrowed down the months for each 3 companies, lets now look at February (EA), March (NTDOY), and August (ATVI).

# In[23]:


df_EA_February_2015 = df_EA_2015[df_EA_2015['Date'].str.contains('2015-01')].copy()
    
plt.figure(figsize=(20,10))
plt.plot(df_EA_February_2015['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)
plt.title("EA Stock Market, Jan 2015")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# There was nothing prominant online in terms of what could have caused this. The closest thing I could find was this climb was partially attributed to Star Wars Battlefront, released in November, and Star Wars The Force Awakens.
# 
# Star Wars - https://en.wikipedia.org/wiki/Electronic_Arts

# In[24]:


df_NTDOY_March_2015 = df_NTDOY_2015[df_NTDOY_2015['Date'].str.contains('2015-03')].copy()
    
plt.figure(figsize=(20,10))
plt.plot(df_NTDOY_March_2015['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)
plt.title("Nintendo Stock Market, Mar 2015")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# Luckily I was able to find an interesting article on this jump, it documents a rather large increase (58%) with the announcement that Nintendo was going to invest in creating Mobile App Games
# 
# Nintendo - https://www.shacknews.com/article/96000/what-is-going-on-with-nintendos-stock

# In[25]:


df_ATVI_August_2015 = df_ATVI_2015[df_ATVI_2015['Date'].str.contains('2015-08')].copy()
    
plt.figure(figsize=(20,10))
plt.plot(df_ATVI_August_2015['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)
plt.title("ATVI Stock Market, August 2015")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# This large jump for Activisions Blizzard was most definitely due to the announcement of their new game World of Warcraft: Legion on the 6th of August 2015, released the following year. While the jump happens a day before the official announcement it can easily be gauged by heavy investors or long time fans as a new expansion is released every 2 years, with the official announcement usually taking place during their Blizzcon event final date, the date of which is known well in advance. While the jump is only ~$3 it can be an easy profit for those heavily invested.
# 
# WoW:Legion - https://en.wikipedia.org/wiki/World_of_Warcraft:_Legion

# ## Yearly Frequency
# At a yearly scale we lose the ability to see certain jumps between weeks/months throughout the year. Overall we can only tell the improvement over last years average.

# In[26]:


# Yearly
for stock in Stocks:
    exec("df_{}_Yearly = df_{}.resample('Y').mean()".format(stock,stock))


# In[27]:


plt.figure(figsize=(40,20))
for stock in Stocks:
    exec("plt.plot(df_{}_Yearly['Close'],marker='o', label='{}',mec='black',markersize=12, linewidth=2)".format(stock,stock))
plt.title("Activision Blizzard Stock, Yearly Mean")
plt.legend(loc=3, prop={'size': 30})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# ## Rolling
# Using the rolling function we can create a slightly smoother graph to recognise trends easier than the daily/monthly ones but with more accurate curves than yearly. Below, we are using rolling set with window at 30 for each month. (Roughly 30 days in a month).

# In[28]:


rm = df_ATVI["Close"].rolling(30).mean()
p = rm.plot(figsize=(15, 10), fontsize=13)


# In the above we notice a dip in late 2015, late 2016, and 3 in 2018. We have already checked the 2015 dip, so lets look at the triple dip in 2018, what caused it and how did Activision Blizzard recover?

# In[29]:


df_ATVI_2018 = df_ATVI[df_ATVI['Date'].str.contains('2018')].copy()
    
plt.figure(figsize=(20,10))
plt.plot(df_ATVI_2018['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)
plt.title("ATVI Stock Market, 2018")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# In[36]:


df_ATVI_2018_March = df_ATVI[df_ATVI['Date'].str.contains('2018-11')].copy()
    
plt.figure(figsize=(20,10))
plt.plot(df_ATVI_2018_March['Close'],marker='o', label='{}',mec='white',markersize=6, linewidth=2)
plt.title("ATVI Stock Market, 2018")
plt.legend(loc=0, prop={'size': 15})
plt.grid(True)
plt.ylabel('Close Price')
plt.xlabel('Year')
plt.show()


# the first 2 dips were caused by an error in reporting on a news network that had accidentally reported figures for stock in 2017 and not 2018. The market was closed to allow time for this correction to be made before any further damage could be done to their market. Next, in November, there was a huge loss as Blizzard had lost its 2nd high profile employee to Twitter. They had announced the release of Diablo for PC (highly criticised as the company not knowing its audience of PC Gamers), and then tied with the news the Heroes of the Storm would be taking a back burner, redundancies were announced, and to top it off the new release of Fortnite in the year meant that it was collecting a large section of the gaming market. While a lot of people may panic at the large decline but the largest drop (as a %) was after the release of Wrath of the Lich King in November 2008, dropping ~55%. This is however the largest drop as a figure by the company, nearly $40.
# 
# Incorrect Reporting - https://www.cnbc.com/2018/05/03/activision-blizzard-shares-dive-following-media-report-on-earnings.html
# Redundancy - https://www.pcgamer.com/activision-blizzard-loses-its-second-executive-in-a-week/
# Fortnite - https://www.forbes.com/sites/insertcoin/2018/03/22/analysts-say-activision-stock-is-sinking-thanks-to-fortnite-mania/

# ## Conclusion
# In conclusion, it would appear that EA is the most profitable, Nintendo is the most stable, while Activision/Blizzard showed the most growth. However, now does not appear to be a good time to invest in either as they have all taken a dip within the last quarter. 
