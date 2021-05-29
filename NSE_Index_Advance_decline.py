import datetime
import glob
import os
import pandas as pd
import time
import webbrowser

import json
from nsetools import Nse

nse = Nse()

q = nse.get_advances_declines()
print("indice,advances,declines,unchanged")
for recc in q:
    print(recc["indice"], ',', recc["advances"], ',', recc["declines"], ',', recc["unchanged"])
print(json.dumps(q))
