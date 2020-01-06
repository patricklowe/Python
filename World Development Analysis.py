#!/usr/bin/env python
# coding: utf-8

# # World Bank Development Indicators - Patrick Lowe, 16725829

# In this assignment I will be looking at the World Bank Development Indicators data. Since this is a large dataset with a variety of insights available, I have chosen to narrow it down by asking 5 questions from different categories (i.e. not all relating to population orientated questions). This is so that there is a varied insight into each country, as some may perform better in different sections. To begin, the data will be loaded into a dataframe as a whole, then narrowed down by country into their own Dataframe. From these, I will filter out 'Indicators' that I find interesting to analyize. The dataframe will then be transposed so that it is more easily ready. Using various charts I will try to analyize the following topics:
# - How do gas emissions vary from country to country?
# - What has the population growth been like?
# - Do countries which contribute a higher percentage of their GDP towards education result in a better educated population?
# - How do imports/exports affect a country and what may cause these trends?
# 
# This dataset can be downloaded here:
# http://databank.worldbank.org/data/download/WDI_csv.zip

# To start, we will import all of the libraries necessary

# In[1]:


import os.path
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Before any processing is done, let's ensure that we have the core data file: WDIData

# In[2]:


if not os.path.exists( "WDIData.csv" ):
    print("Missing dataset file - WDIData.csv")


# In[3]:


df_full = pd.read_csv( "WDIData.csv" )


# Now lets check all the countries that have data

# In[4]:


df_full["Country Name"].unique()


# Now lets take only data relating to some countries of interest. For this assignment I will be looking into:
# - Costa Rica
# - Cayman Islands
# - France
# - Germany
# - Greece
# - Italy
# - Ireland
# - New Zealand
# - United States
# - Australia

# Firstly, view the full dataset and determine what columns may be redundant

# In[5]:


df_full.head(5)


# From this view, it appears that Country Code can be dropped as we already have a slightly more descriptive version under Contry Name. We can also remove Indicator Code as Indicator Name is better understood.

# In[6]:


df_full = df_full.drop(['Country Code'], axis=1)
df_full = df_full.drop(['Indicator Code'], axis=1)


# In[7]:


# Creates a new DataFrame for each country of Interest
countries_with_Underscore = ['Costa_Rica','Cayman_Islands','France','Germany','Greece','Italy','Ireland','New_Zealand','United_States','Australia']

for country in countries_with_Underscore:
     exec('df_{} = pd.DataFrame()'.format(country))


# In[8]:


# Fill each new country's dataframe with their relevant information
countries_of_Interest = ['Costa Rica','Cayman Islands','France','Germany','Greece','Italy','Ireland','New Zealand','United States','Australia']
i = 0

for country in countries_with_Underscore:
    selected_country = countries_of_Interest[i]
    exec("df_{} = df_full[df_full['Country Name'] == '{}'].copy()".format(country,selected_country))
    i += 1


# Now, lets see our new table (without Country Code column, or Indicator Code column).

# In[9]:


df_Ireland.head(5)


# Next, we will create a new dataframe that contains all the interesting Indicators that may help us answer out initial questions.

# In[10]:


# Get our dataframe unique names again
countries_with_Underscore = ['Costa_Rica','Cayman_Islands','France','Germany','Greece','Italy','Ireland','New_Zealand','United_States','Australia']

# Initialize each new dataframe of individual countrys' interests
for country in countries_with_Underscore:
    exec("df_{}_Interests = df_{}.loc[df_{}['Indicator Name'] == 'Adjusted net national income (annual % growth)']".format(country,country,country))

# append the data that helps answer our questions into a new Dataframe
Indicators = [
'Electric power consumption (kWh per capita)',
'Agricultural methane emissions (% of total)',
'Total greenhouse gas emissions (kt of CO2 equivalent)',
'Agricultural nitrous oxide emissions (% of total)',
'CO2 emissions (kt)',
'CO2 emissions from gaseous fuel consumption (% of total)',
'CO2 emissions from liquid fuel consumption (% of total)',
'CO2 emissions from manufacturing industries and construction (% of total fuel combustion)',
'CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion)',
'CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion)',
'CO2 emissions from solid fuel consumption (% of total)',
'CO2 emissions from transport (% of total fuel combustion)',
'Mortality rate attributed to household and ambient air pollution, age-standardized (per 100,000 population)',
'Mortality rate attributed to household and ambient air pollution, age-standardized, female (per 100,000 female population)',
'Mortality rate attributed to household and ambient air pollution, age-standardized, male (per 100,000 male population)',
'Mortality rate attributed to unintentional poisoning (per 100,000 population)',
'Mortality rate attributed to unintentional poisoning, female (per 100,000 female population)',
'Mortality rate attributed to unintentional poisoning, male (per 100,000 male population)',
'Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)',
'Population ages 0-14 (% of total)',
'Population ages 15-64 (% of total)',
'Population ages 65 and above (% of total)',
'Population density (people per sq. km of land area)',
'Population growth (annual %)',
'Population, female',
'Population, female (% of total)',
'Population, male',
'Population, male (% of total)',
'Population, total',
'Birth rate, crude (per 1,000 people)',
'Death rate, crude (per 1,000 people)',
'GDP growth (annual %)',
'Government expenditure on education, total (% of GDP)',
'Government expenditure per student, primary (% of GDP per capita)',
'Government expenditure per student, secondary (% of GDP per capita)',
'Government expenditure per student, tertiary (% of GDP per capita)',
'Exports of goods and services (% of GDP)',
'Food exports (% of merchandise exports)',
'Food imports (% of merchandise imports)',
'Fuel exports (% of merchandise exports)',
'Fuel imports (% of merchandise imports)',
'ICT goods exports (% of total goods exports)',
'ICT goods imports (% total goods imports)',
"Educational attainment, at least Bachelor\\'s or equivalent, population 25+, total (%) (cumulative)",
'Educational attainment, at least completed lower secondary, population 25+, total (%) (cumulative)',
'Educational attainment, at least completed post-secondary, population 25+, total (%) (cumulative)',
'Educational attainment, at least completed primary, population 25+ years, total (%) (cumulative)',
'Educational attainment, at least completed short-cycle tertiary, population 25+, total (%) (cumulative)',
'Educational attainment, at least completed upper secondary, population 25+, total (%) (cumulative)',
"Educational attainment, at least Master\\'s or equivalent, population 25+, total (%) (cumulative)",
'Educational attainment, Doctoral or equivalent, population 25+, total (%) (cumulative)',]
for country in countries_with_Underscore:
    k = 0
    for element in Indicators:
        selected_Indicator = Indicators[k]
        exec("df_{}_Interests = df_{}_Interests.append(df_{}.loc[df_{}['Indicator Name'] == '{}'], ignore_index=True)".format(country,country,country,country,selected_Indicator))
        k += 1


# Next we will rotate the table so that the Indicator names become column titles, and the years become row entries

# In[11]:


new_Transpose = ['CR','CI','Fr','Ge','Gr','It','Ir','NZ','US','Au']
i = 0
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[i]
    exec("df_{}_T = df_{}_Interests.transpose()".format(Transpose_Name,country))
    i += 1


# Lets check our new transposed table, to check that a) everything has converted correctly, and b) check what needs to be configured.

# In[12]:


df_Ir_T.head(3)


# Lets remove the first row of each transposed dataframe, since we now know that each country is in their respective dataframe

# In[13]:


# remove first row(country names) from each transposed dataframe
i = 0
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[i]
    exec("df_{}_T = df_{}_T.iloc[1:]".format(Transpose_Name,Transpose_Name))
    i += 1


# In[14]:


# rename the columns after the new first row (Indicator Names), since the transpose has distorted them
i = 0
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[i]
    exec("df_{}_T.columns = df_{}_T.iloc[0]".format(Transpose_Name,Transpose_Name))
    i += 1


# In[15]:


# remove first row again, indicator names which are now the column headers
i = 0
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[i]
    exec("df_{}_T = df_{}_T.iloc[1:]".format(Transpose_Name,Transpose_Name))
    i += 1


# In[16]:


# View Table
df_Ir_T.head(3)


# Now, lets try plot some sample information

# In[17]:


plt.figure(figsize=(40,20))
plt.plot(df_Ir_T['Electric power consumption (kWh per capita)'], marker='o', markerfacecolor='blue', markersize=12, color='gold', linewidth=2)


# This graph shows the Energy Consumption (KWh) across all the years. Overall, the energy consumption increases but after some quick research the minor dips could correlate to recessions that hit Ireland (1975, 1980s, 2007). This was most likely due to conservation of energy since there was a high price of energy per KWh. 
# - https://en.wikipedia.org/wiki/Economic_history_of_the_Republic_of_Ireland#1980_to_early_1990s
# - https://en.wikipedia.org/wiki/Economy_of_the_Republic_of_Ireland

# # Q1. How do different gas emissions vary from country to country
# For this questions, our goal is to view who are the largest contributors of gas emissions (Methane, from Agriculture) 

# In[18]:


p = 0
plt.figure(figsize=(50,40))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['Agricultural methane emissions (% of total)'],marker='o', label='{}',mec='black',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1

# For repositioning check: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
# Change size property for legend below, it is difficult to get everything to fit properly, may be due my small screen though.
plt.title("% of Methane from Agriculture")
plt.legend(loc=3, prop={'size': 30})
plt.grid(True)
plt.ylabel('% of Methane')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.show()


# In the above graph we can see the methane emissions from sources such as animals, their waste, rice production, agricultural waste burning, and savannah burning. Immediately noticible is the Cayman Islands taking a severe drop from 1983 in Agricultural Methane emssions. While I was not able to find any evidence online as to what could have caused this, I believe that it is possible that better agricultural techniques were sourced thanks to a 300% tourism boom that the Cayman Islands experienced in the previous years. As mentioned in this article, agriculture began to soar from 1984, yet their emissions dropped.
# - http://www.fao.org/docrep/017/ap664e/ap664e.pdf
# 
# What is interesting to note also is that Costa Rica takes a decline from 1994 onwards. This is most likely due to the a change in their constitution in article 50, where "every person has the right to a healthy and ecologically balanced environment, being therefore entitled to denounce any acts that may infringe the said right and claim redress for the damage caused". 
# - https://www.ohchr.org/EN/HRBodies/HRC/RegularSessions/Session25/Documents/A-HRC-25-53-Add1_fr.doc
# 
# Greece is another country which has been declining in methane since 1974. This could be due to improvements in farming techniques, similair to the Cayman Islands. Such techniques would not even need to be costly, from covering manuer with a light material to prevent direct sunlight/air exposure, to applying slurry on land closer to the surface to prevent agitation releasing more methane.
# - http://www.europarl.europa.eu/RegData/etudes/note/join/2014/513997/IPOL-AGRI_NT(2014)513997_EN.pdf
# 
# Ffinaly, another factor may be the Kyoto Protocol, an environmental agreement from 1997 by most of the groups in the United Nations Framework Convention on Climate Change (UNFCCC), and its prime goal is to curb CO2 emissions globally. 
# - WDISeries.csv line 405

# Lets see if another gas emission follows a similair trend.

# In[19]:


p = 0
plt.figure(figsize=(40,30))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['CO2 emissions from transport (% of total fuel combustion)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("% of CO2 from Transport")
plt.legend(loc=0, prop={'size': 30})
plt.grid(True)
plt.ylabel('% of CO2, Transport')
plt.xlabel('Year')
plt.xticks(["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.show()


# From the previous graph on Methane production, we notice that the Cayman Islands has no data, and therefore we cannot compare or analize with the drop from 1983 in Agricultural Methane emssions.
# 
# Previously we saw that Costa Rica takes a decline from 1994 onwards in Methane production, but here we can see an overall increase in CO2 emissions from transport at Costa Rica. This could show that it was not the ammendment mentioned in the previous section that caused the methane to drop, but could be (like with other countries) the development in modern and improved farming techniques that caused it to drop. Or perhaps their citizens didn't believe that CO2 from transport was as major a concern.
# 
# Greece is another country which has been declining in CO2 since 1964. Their CO2 then began to climb again from 1975, returning to a similair CO2 emission level as in 1963/64.
# 
# While this data shows that some countries have dropped in CO2/Methane emissions from year to year, this only indicates that the source of CO2 overall was coming from transport less (or more). For example, Greece had a decline of CO2 coming from transport but we can easily find that the overall production of CO2 increased throughout the years. This is likely due to public transport reducing lone driver cars on the road (less emissions, since more people can travel in bulk), improvement in transport of goods etc, while more production companies could contribute to the overall CO2 production. The graph below shows the levels of CO2 in Greece across the same timeline.

# In[20]:


plt.figure(figsize=(20,10))
plt.plot(df_Gr_T['CO2 emissions (kt)'])
plt.legend(loc=0, prop={'size': 11})
plt.grid(True)
plt.ylabel('CO2 Emissions (KT)')
plt.xlabel('Years')
plt.xticks(["1960","1970","1980","1990","2000","2009"])
plt.show()


# From the above, we can see a overly steady increase of CO2 emissions, until ~2005 when they start to drop. This may be due to climate change becoming a threat. We also have the ability to look into which type of fuel consumption is causing the most pollution in Greece (and other countries, but for ease I will continue with Greece).

# In[21]:


CO2 = [
'CO2 emissions from gaseous fuel consumption (% of total)',
'CO2 emissions from liquid fuel consumption (% of total)',
'CO2 emissions from solid fuel consumption (% of total)',
]

p = 0
plt.figure(figsize=(50,40))
for emission in CO2:
    em_Type = CO2[p]
    exec("plt.plot(df_Gr_T['{}'],marker='o', label='{}',mec='black',markersize=17, linewidth=2)".format(em_Type,em_Type))
    p += 1

plt.title("% of Methane from Agriculture")
plt.legend(loc=1, prop={'size': 40})
plt.grid(True)
plt.ylabel('% of Methane')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.show()


# Here we can see that Gaseous fuel consumption is almost non-existent, up until ~1997 when it starts to take off, although still relatively small. What we can also see is that Liquid Fuel consumption is the prime cause of CO2 emissions, with Solid Fuel trailing behind. A lovely trend to observe is how these almost mirror eachother, when one increases the other decreases, until Gas Fuel is introduced, it appears to affect Solid Fuel the most. From this research it is clear that in order for Greece to make the most dramatic changes to their overall CO2 production, their main focus should be on Liquid Fuel consumption.

# # What has the population growth been like
# For this question we will look at data relating to the birth rate, death rate, and population by gender/age.

# In[22]:


p = 0
plt.figure(figsize=(40,30))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['Population growth (annual %)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("% of CO2 from Transport")
plt.legend(loc=0, prop={'size': 30})
plt.grid(True)
plt.ylabel('% of CO2, Transport')
plt.xlabel('Year')
plt.xticks(["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.show()


# What is eye-catching about this graph is the sporadic changes in population growth on the Cayman Islands. This graphs seems to show huge population growth and decline (relative to other nations), but once you consider they have a population of ~65,000 in the Cayman Islands, even the slightest change of population would show drastic results in this chart. 
# 
# Another interesting fact to look at is the population growth of Ireland in 2007, when the recession hit. It took a staggering drop, but Australia seems to take an almost equal rise in comparison. This is likely due to nurses and builders (primarily) moving abroad to a better life.
# 
# The remainder of these countries appear to fluctuate evenly, but if you notice that Germany takes a relatively large drop in growth (in the minus in fact) in 2011. This could be due to their introduction of the Austerity Program, which aimed to save €80 Billion from 2011 to 2014. This meant there would be a reduction in civil service jobs, jobless benefits, etc (1st reference). Another reason for this drop (or in combination with) is that Germany had not completed a full census since 1987, which was strongly apposed. The 2011 was the first fully conducted census of their population since then, and they had miscalculated their residents by 1.5 Million residents (~1.8% of their population)(2nd reference). The reason the growth could be so high after this period, is that firstly with the new census data the growth % is unlikely to vary greatly along the 0% line. Secondly, with their figures lower than expected Germany could be looking for faster ways to increase their working population, i.e. immigration. They experienced a rise of immigration to Germany from 2012 onwards. (3rd reference below)
# 
# - http://www.spiegel.de/international/germany/radical-cutbacks-german-government-agrees-on-historic-austerity-program-a-699229.html
# - https://www.nytimes.com/2013/06/01/world/europe/census-shows-new-drop-in-germanys-population.html
# - https://www.migrationpolicy.org/article/new-reality-germany-adapts-its-role-major-migrant-magnet?gclid=CjwKCAiAqt7jBRAcEiwAof2uKwBMOuuYfhqPWyQRuEg9_tY-DIXgEd_JL_azGWUtERLN__bIYPiSahoCz_YQAvD_BwE

# In[23]:


plt.figure(figsize=(30,10))
plt.plot(df_Ge_T['Population density (people per sq. km of land area)'],marker='o', label='Germany',markersize=8, linewidth=1)
plt.title("Population Density, Germany")
plt.legend(loc=1, prop={'size': 30})
plt.grid(True)
plt.ylabel('Density, per sq. KM')
plt.xlabel('Year')
plt.xticks(["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.show()


# We can see the large rise in population density around 1990, when Germany became unified, then the drop in density at 2011 since their estimates were off from the last census in 1987.

# # Do countries who countribute a higher percentage of their GDP towards education result in a better educated population?
# The goal of this question is to see which countries have better educated population based on the their contirbution of GDP towards education. The level of education is broken up into primary, secondary, and tertirary education.

# In[24]:


p = 0
plt.figure(figsize=(20,10))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['Government expenditure on education, total (% of GDP)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("Expenditure on Education, % of total GDP")
plt.legend(loc=0, prop={'size': 10})
plt.grid(True)
plt.ylabel('% of GDP on Education')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"])
plt.show()


# We have finally come across data with some missing values. This could be tricky as some countries have very sporadic data, while others are only missing a few years. Lets look at Ireland.

# In[25]:


df_Ir_T['Government expenditure on education, total (% of GDP)'].head(25)


# We can see that a lot of the early years have no data. Lets fill these NaN rows with the mean percentage of the overall expenditure on education.

# In[26]:


df_Ir_T['Government expenditure on education, total (% of GDP)'] = df_Ir_T['Government expenditure on education, total (% of GDP)'].fillna((df_Ir_T['Government expenditure on education, total (% of GDP)'].shift() + df_Ir_T['Government expenditure on education, total (% of GDP)'].shift(-1))/2)


# In[27]:


plt.figure(figsize=(20,10))
plt.plot(df_Ir_T['Government expenditure on education, total (% of GDP)'],marker='o', label='Ire',markersize=12, linewidth=2)
plt.title("Expenditure on Education, % of total GDP")
plt.legend(loc=0, prop={'size': 10})
plt.grid(True)
plt.ylabel('% of GDP on Education')
plt.xlabel('Year')
plt.xticks(["1975","1980","1985","1990","1995","2000","2005","2010","2015"])
plt.show()


# While this is not the best or most accurate way to fill in the data it does give us a better idea. We can see that 1975 now has a value, and so does 1997 which were both previously missing. This way of filling in data does however give a good estimate on missing data, the problem occurs when multiple data is missing through a period, or a random missing interval hits an unknown spike, just like Germany with population growth in 2011.

# In[28]:


# Update missing values with the average between previous and next known values.
i = 0
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[i]
    exec("df_{}_T['Government expenditure on education, total (% of GDP)'] = df_{}_T['Government expenditure on education, total (% of GDP)'].fillna((df_{}_T['Government expenditure on education, total (% of GDP)'].shift() + df_{}_T['Government expenditure on education, total (% of GDP)'].shift(-1))/2)".format(Transpose_Name,Transpose_Name,Transpose_Name,Transpose_Name))
    i += 1


# In[29]:


# View the newly updated data
p = 0
plt.figure(figsize=(20,10))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['Government expenditure on education, total (% of GDP)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("Expenditure on Education, % of total GDP")
plt.legend(loc=0, prop={'size': 10})
plt.grid(True)
plt.ylabel('% of GDP on Education')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"])
plt.show()


# As we can see, there was a lot of missing data that was replaced with estimates. Lets remove countries that have too little data to work with; Costa Rica, Cayman Islands, Germany, United States. 

# In[30]:


# View more ideal countries
ideal_Transpose = ['Fr','Gr','It','Ir','NZ','Au']
ideal_Countries = ['France','Greece','Italy','Ireland','New_Zealand','Australia']
p = 0
plt.figure(figsize=(20,10))
for country in ideal_Countries:
    Transpose_Name = ideal_Transpose[p]
    exec("plt.plot(df_{}_T['Government expenditure on education, total (% of GDP)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("Expenditure on Education, % of total GDP")
plt.legend(loc=0, prop={'size': 10})
plt.grid(True)
plt.ylabel('% of GDP on Education')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"])
plt.show()


# An interesting note is the increase of expenditure on education in 2007/2008. This may not mean that the countries have contributed more monetary value to education, but could show that the GDP has reduced, education spending has remained fairly similair but as a % it appears to have increased. Lets look at Ireland.

# In[31]:


edu_level = [
'Government expenditure per student, primary (% of GDP per capita)',
'Government expenditure per student, secondary (% of GDP per capita)',
'Government expenditure per student, tertiary (% of GDP per capita)'
]

p = 0
plt.figure(figsize=(20,10))
for education in edu_level:
    edu_Type = edu_level[p]
    exec("plt.plot(df_Ir_T['{}'],marker='o', label='{}',mec='black',markersize=17, linewidth=2)".format(edu_Type,edu_Type))
    p += 1
plt.title("% of Expenditure on Education, Ireland")
plt.legend(loc=2, prop={'size': 13})
plt.grid(True)
plt.ylabel('% of Expenditure')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.xlim("1995","2018")
plt.show()


# In[72]:


df_Ir_T['Educational attainment, at least completed lower secondary, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='gold',fontsize=14)
df_Ir_T['Educational attainment, at least completed upper secondary, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='skyblue',fontsize=14)
df_Ir_T['Educational attainment, at least completed post-secondary, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='green',fontsize=14)
df_Ir_T['Educational attainment, at least Bachelor\'s or equivalent, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='black',fontsize=14)
df_Ir_T['Educational attainment, at least Master\'s or equivalent, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='blue',fontsize=14)
df_Ir_T['Educational attainment, Doctoral or equivalent, population 25+, total (%) (cumulative)'].plot(kind='bar',figsize=(14,7),color='red',fontsize=14)

plt.title("% of Expenditure on Education, Ireland")
plt.legend(loc=2, prop={'size': 13})
plt.ylabel('% of Completion')
plt.xlabel('Year')


# From this we can see that more citizens in ireland are completing the basic levels of education, and as the years go on more are going to, and completing higher education. This would appear to show that expenditure in education can increase the number of citizens that aim for a higher degree. We can see in 1991 that a lot more students finished their Leaving Cert, wereas a decade before hand it was primarily Juniour Cert levels. As the years increase and more funding is supplied, these same adults may now choose to persue more degrees of varying levels.

# # What trends do imports/exports have?
# The goal here is to see how imports/exports could affect a country, and what caused these trends

# In[83]:


p = 0
plt.figure(figsize=(40,30))
for country in countries_with_Underscore:
    Transpose_Name = new_Transpose[p]
    exec("plt.plot(df_{}_T['Food exports (% of merchandise exports)'],marker='o', label='{}',markersize=12, linewidth=2)".format(Transpose_Name,country))
    p += 1
plt.title("% of Food Exports")
plt.legend(loc=0, prop={'size': 30})
plt.grid(True)
plt.ylabel('% of Food Exports, from merchandise exports')
plt.xlabel('Year')
plt.xticks(["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"])
plt.show()


# The most notible country here is Costa Rica, as it takes a large dive between 1995 to 2000. Lets take a closer look at Costa Rica.

# In[90]:


edu_level = [
'Exports of goods and services (% of GDP)',
'Food exports (% of merchandise exports)',
'Food imports (% of merchandise imports)',
'Fuel exports (% of merchandise exports)',
'Fuel imports (% of merchandise imports)',
'ICT goods exports (% of total goods exports)',
'ICT goods imports (% total goods imports)'
]

p = 0
plt.figure(figsize=(20,10))
for education in edu_level:
    edu_Type = edu_level[p]
    exec("plt.plot(df_CR_T['{}'],marker='o', label='{}',mec='black',markersize=17, linewidth=2)".format(edu_Type,edu_Type))
    p += 1
plt.title("% of Expenditure on Education, Ireland")
plt.legend(loc=1, prop={'size': 13})
plt.grid(True)
plt.ylabel('% of Expenditure')
plt.xlabel('Year')
plt.xticks(["1970","1975","1980","1985","1990","1995","2000","2005","2009"])
plt.xlim("1990","2005")
plt.show()


# As we can see, when comparing it with other exports, they remain relatively unaffected, and looking at the imports, there was no import goods that may have balanced out the exports dropping. From my research I was not able to find any source that would suggest exports in Costa Rica to drop significantly. From a few articles I did find, Pineapples & Banana's were the main source of food exports at over 50%, while coffee was a notorious runner up, however coffee production slowed down immensely in since then, fruit exports has more than made up for it. Overall, I don't understand why this drop is being shown.
# - http://www.fao.org/3/y4632e/y4632e0a.htm

# # Conclusion
# Overall, I enjoyed being able to explore such a vast dataset. I decided to narrow it down and compare country by country, selecting countries random. Most of the early years had no data recorded as it is possible those questions only became recently asked on the census. Some percentages were using a landmark year as a baseline for change, for example the CO2 emissions change had a baseline of 2010, so previous years would show a decline, instead of an incline on years gone by. This could be avoided by downloading their particular dataset relevant to the year you'd like to use as a baseline. 
# 
# In addition to my previous observations, noted in the markdowns, I found it interesting to see how countries performed overall, and how some even changed my prejudice views on them, Cayman Islands population growth, Costa Rica's gas emissions etc. I believe that line charts were an easy and legible way of viewing this data, although in some cases bar charts may have worked better, perhaps more in ranking countries by year. I found bar charts difficult to create with a loop, and since most of my questions were to see linear changes I stuck with line charts primarily.
# 
# Further observations could be made by including a larger set of countries to compare to, perhaps group my region (Europe, Asia, America, etc) and compare thusly. Having more data to work from would also allow for better interpretations, some countries had a vast amount of data available but would hit indicators that received no data. Again, this could be down to it being a new indicator so that data is not realistically available.
# 
# I hope that viewers of this notebook will easily be able to understand 1) how the data was collected, stored, and transformed to be better utilised. 2) Gain some valuable insights into trending areas of interest, and 3) be eager to continue, improve, or even adjust the research found here.
