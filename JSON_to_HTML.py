
q = nse.get_advances_declines()
from json2html import *
HTML_Index_adv_decline=json2html.convert(json = q)
print(HTML_Index_adv_decline)

q = nse.get_top_gainers()
from json2html import *
HTML_top_gainers=json2html.convert(json = q)
print(HTML_top_gainers)
