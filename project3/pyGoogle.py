# import pandas as pd
# from pytrends.request import TrendReq

# pytrends = TrendReq(hl='en-US-state', tz=360)


# pytrend = TrendReq(hl='en-US', tz=360)
# keywords = ['super mario', 'fortnite', 'pokemon', 'pubg','moderna stock']
# kw_list=keywords


# pytrend.build_payload(
#      kw_list=keywords,
#      cat=0,
#      timeframe='today 5-y',
#      geo='US-FL',
#      gprop='')
# #data = pytrend.interest_over_time()

# data = pytrend.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)


# data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

from pytrends.request import TrendReq
import pandas as pd
import time
import csv 

startTime = time.time()
time.sleep(1)
pytrend = TrendReq(hl='en-US', tz=360)

colnames=["keywords"]

df = pd.read_csv("keyword_list.csv", names=colnames) #reads from file and obtain a list of keywords to search
df2 = df["keywords"].values.tolist()
	
df2.remove("Keywords")

dataset = []

for x in range(0, len(df2)): #obtaining different data for each state 
	keywords = [df2[x]]
	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30', #data ranges from 2010 to 2020, data from the beginning of every month 
	# 	geo ='US-AL')
	# data = pytrend.interest_over_time()
	# stateName = []
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)


	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-AK')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-AZ')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	pytrend.build_payload(
		kw_list=keywords,
		cat=0,
		timeframe='2010-01-01 2020-10-30',
		geo ='US-AR')
	data = pytrend.interest_over_time()
	if not data.empty:
		data = data.drop(labels=['isPartial'], axis='columns')
		dataset.append(data)

	pytrend.build_payload(
		kw_list=keywords,
		cat=0,
		timeframe='2010-01-01 2020-10-30',
		geo ='US-CA')
	data = pytrend.interest_over_time()
	if not data.empty:
		data = data.drop(labels=['isPartial'], axis='columns')
		dataset.append(data)

	pytrend.build_payload(
		kw_list=keywords,
		cat=0,
		timeframe='2010-01-01 2020-10-30',
		geo ='US-CO')
	data = pytrend.interest_over_time()
	if not data.empty:
		data = data.drop(labels=['isPartial'], axis='columns')
		dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-CT')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-DE')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-FL')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-GA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-HI')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-ID')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-IL')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-IN')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-IA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-KS')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-KY')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-LA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-ME')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MD')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MI')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MN')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MS')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MO')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-MT')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NE')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NV')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NH')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NJ')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NM')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NY')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-NC')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-ND')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-OH')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-OK')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-OR')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-PA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-RI')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-SC')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-SD')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-TN')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-TX')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-UT')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-VT')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-VA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)


	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-WA')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-WV')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-WI')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)

	# pytrend.build_payload(
	# 	kw_list=keywords,
	# 	cat=0,
	# 	timeframe='2010-01-01 2020-10-30',
	# 	geo ='US-WY')
	# data = pytrend.interest_over_time()
	# if not data.empty:
	# 	data = data.drop(labels=['isPartial'], axis='columns')
	# 	dataset.append(data)


for x in range(0, len(df2)):
	# stateName.append("AL")
	# stateName.append('AK')
	# stateName.append('AZ')
	stateName.append("AR")
	stateName.append('CA')
	stateName.append("CO")
	# stateName.append('CT')
	# stateName.append("DE")
	# stateName.append("FL")
	# stateName.append('GA')
	# stateName.append('HI')
	# stateName.append("ID")
	# stateName.append('IL')
	# stateName.append("IN")
	# stateName.append('IA')
	# stateName.append("KS")
	# stateName.append('KY')
	# stateName.append("LA")
	# stateName.append('ME')
	# stateName.append("MD")
	# stateName.append('MA')
	# stateName.append("MI")
	# stateName.append('MN')
	# stateName.append("MS")
	# stateName.append('MO')
	# stateName.append("MT")
	# stateName.append('NE')
	# stateName.append("NV")
	# stateName.append('NH')
	# stateName.append("NJ")
	# stateName.append('NM')
	# stateName.append("NY")
	# stateName.append('NC')
	# stateName.append("ND")
	# stateName.append('OH')
	# stateName.append("OK")
	# stateName.append('OR')
	# stateName.append('PA')
	# stateName.append('RI')
	# stateName.append('SC')
	# stateName.append('SD')
	# stateName.append('TN')
	# stateName.append('TX')
	# stateName.append('UT')
	# stateName.append('VT')
	# stateName.append('VA')
	# stateName.append('WA')
	# stateName.append('WV')
	# stateName.append('WI')
	# stateName.append('WY')

result = pd.concat(dataset, axis=1, keys=stateName)

result.to_csv('search_trends2.csv')







