import datetime
import glob
import os
import pandas as pd
import time
import webbrowser

import json
from nsetools import Nse
nse = Nse()

data = []
os.chdir('C:\\Users\\shrio\\Desktop\\bhav_files\\')

q = nse.get_top_gainers()

# print(json.dumps(q))
# print("symbol", ',', "ltp", ',', "netPrice", ',', "openPrice", ',', "highPrice", ',', "previousPrice", ',',
#       "tradedQuantity", ',', "turnoverInLakhs")
for recc in q:
    del recc['series']
    del recc['lastCorpAnnouncement']
    del recc['lastCorpAnnouncementDate']
    print(recc)

with open('thiya_test.json','w') as ff:
    json.dump(q,ff)
