
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
# 40有坑
def parse_tr(tr, year):
    tds = tr.find_all('td')
    if len(tds) != 4: return None
    country = tds[1].string
    states = tds[2].string
    val = tds[3].string
    val = val.split('(')[-1].split(')')[0]
    return (country, states, val, year)

years = range(1959, 2019)
res = []
for year in years:
    item = []
    print(year,'-'*50)
    url = 'https://www.kuaiyilicai.com/stats/global/yearly/g_population_total/{}.html'.format(year)
    response = requests.get(url = url)
    if response.status_code != 200:
        print(response.status_code)
    text = response.text
    soup = BeautifulSoup(text, 'xml')
    tbody = soup.find_all('tbody')[0]
    trs = tbody.find_all('tr')
    # print("trs", len(trs))
    for tr in trs[:39]:
        res.append(parse_tr(tr,year))
    time.sleep(1)

dataframe = pd.DataFrame(data = res, columns = ['country', 'states', 'val', 'year'])
dataframe.to_csv('population_data.csv')
# suceess
# print(response.text)
