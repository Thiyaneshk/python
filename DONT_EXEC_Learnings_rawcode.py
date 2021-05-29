import datetime
import glob
import os
import pandas as pd
import time
import webbrowser

import json
from nsetools import Nse
nse = Nse()

################################################################
# Below lines are for Bhav download and concat
################################################################
#
# begin = datetime.date(2021, 5, 1)
# end = datetime.date(2021, 5, 10)
#
# # download_folder = r"C:\Users" + "\\" + "shrio" + "\\" + "Downloads" + "\\"
# download_folder = r"C:\Users" + "\\" + "shrio" + "\\" + "Desktop" + "\\" + "bhav_files" + "\\"
#
# file_patternn = str(download_folder) + str('sec_bhavdata_full_*.csv')
# fileList = glob.glob(file_patternn)
# for filePath in fileList:
#     try:
#         os.remove(filePath)
#     except:
#         print("Error while deleting file : ", filePath)
#
# next_day = begin
# while True:
#     if next_day > end:
#         break
#     dayy = str(next_day.day)
#     l_day = dayy.zfill(2)
#     montth = str(next_day.month)
#     l_month = montth.zfill(2)
#
#     myDateFmt = l_day + l_month + str(next_day.year)
#     next_day += datetime.timedelta(days=1)
#     if len(pd.bdate_range(next_day, next_day)) == 1:
#         bhav_url = str('https://archives.nseindia.com/products/content/sec_bhavdata_full_') + str(myDateFmt) + str(
#             '.csv')
#         webbrowser.open(bhav_url)
#
# time.sleep(10)
# Bhav_Master_folder = r"C:\Users" + "\\" + "shrio" + "\\" + "Desktop" + "\\" + "bhav_files" + "\\"
#
# file_patternn = str(download_folder) + str('sec_bhavdata_full_*')
# fileList = glob.glob(file_patternn)
#
# os.chdir(Bhav_Master_folder)
# combined_csv = pd.concat([pd.read_csv(f) for f in fileList])
# combined_csv.to_csv("Bhav_Master.csv", index=False, encoding='utf-8-sig')
#
################################################################
# Bhav download code ends
################################################################

# print ('Thiyanesh here... test JSON data read from URL')
#
# # # import urllib library
# from urllib.request import urlopen
#
# # import json
# import json
#
# # store the URL in url as
# # parameter for urlopen
# url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/fnoGainers1.json'
#
# # store the response of URL
# response = urlopen(url)
#
# # storing the JSON response
# # from url in data
# data_json = json.loads(response.read())
#
# # print the json response
# print(data_json)
#

# using nsetools packages!
# import json
# from nsetools import Nse
# nse = Nse()
# from pprint import pprint
# # q = nse.get_quote('infy')
# q = nse.get_top_gainers()
# # pprint(q)
#
#
# df = pd.json_normalize(q)
# # print ( str(df["symbol"]) + str(df["ltp"]))
# print (df["symbol"])


# print (df["lastCorpAnnouncement"])
# print (df["tradedQuantity"])
# json_data= print(json.dumps(q))
# print(df)



#
# # download_folder = r"C:\Users" + "\\" + "shrio" + "\\" + "Downloads" + "\\"
# download_folder = r"C:\Users" + "\\" + "shrio" + "\\" + "Desktop" + "\\" + "bhav_files" + "\\"
#
# file_patternn = str(download_folder) + str('Testttt.csv')
# import json
# import csv
# #
#
# JSON_url="http://api.plos.org/search?q=title:DNA"
# f = open(JSON_url)
# data = json.load(f)
# f.close()
#
# f = open(file_patternn)
# csv_file = csv.writer(f)
# for item in data:
#     csv_file.writerow(item)
#
# f.close()
#
# # json_file = r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json'
# # print (json_file)
# df = pd.read_json (q)
# # df.to_csv (r'C:\Users\shrio\Desktop\bhav_files\test_json_convert.csv', index = None, header=True)

#
# import pandas as pd
#
# pd.set_option('display.max_columns', 50)  # display columns
# df = pd.read_json(r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json')
# print(df)

##$$$$$$$$$$ below code is working ....reads JSON file and displays


q = nse.get_top_gainers()
print("symbol", ',', "ltp", ',', "netPrice", ',', "openPrice", ',', "highPrice", ',', "previousPrice", ',',
      "tradedQuantity", ',', "turnoverInLakhs")
for recc in q:
    print(recc["symbol"], ',', recc["ltp"], ',', recc["netPrice"], ',', recc["openPrice"], ',', recc["highPrice"], ',',
          recc["previousPrice"], ',', recc["tradedQuantity"], ',', recc["turnoverInLakhs"])

print(json.dumps(q))


#
# with open(r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json') as json_file:
#     data1 = json.load(json_file)
#     # print(data1)
#     # print (type(data1 ))
# print (   "symbol", ',', "open" , ',',  "dayHigh" , ',',  "dayLow" , ',',  "lastPrice"  , ',', "pChange",',', "perChange365d" )
# for recc in data1["data"]:
#     print (  recc["symbol"], ',', recc["open"], ',', recc["dayHigh"], ',', recc["dayLow"],',', recc["lastPrice"] ,',', recc["pChange"] ,',',  recc["perChange365d"])

###########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
# import pandas as pd
#
# pd.set_option('display.max_columns', 50)  # display columns
# df = pd.read_json(r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json')
# df.to_csv("pokedex.csv")



# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# print(json.dumps(x))


#
# import json
# import pandas as pd
# from pandas.io.json import json_normalize
# data = json.load(open(r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json'))
# df = pd.DataFrame(data["data"])
# print (df)
# print (df["symbol"])
#

# df = json_normalize(data, 'symbol').assign(**data['identifier'])
# print (df)
#
# df = pd.DataFrame(data["symbol"])
#
#
# import json
#
# with open(r'C:\Users\shrio\Desktop\bhav_files\sample_JSON_NSE.json') as project_file:
#     data = json.load(project_file)
#
# df = pd.json_normalize(data)
#
# print(df)
