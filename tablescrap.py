import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
url = "URL_with_wiki_table"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table',{'class':"wikitable"})
year = []
date = []
treatyname = []
altname = []
statute = []
landcessions = []
tribe = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')

        if len(cells) > 1:
            yr = cells[0]
            year.append(yr.text.strip())

            dat = cells[1]
            date.append(dat.text.strip())

            treatynam = cells[2]
            treatyname.append(treatynam.text.strip())

            altnam = cells[3]
            altname.append(altnam.text.strip())

            statut = cells[4]
            statute.append(statut.text.strip())

            landcession = cells[5]
            landcessions.append(landcession.text.strip())

            trib = cells[6]
            tribe.append(trib.text.strip())

column_names = ["year", "date", "treatyname", "altname", "statute", "landcessions", "tribe"]
df = pd.DataFrame(list(zip(year,date, treatyname, altname, statute, landcessions, tribe)), columns=["Year","Date", "Treaty Name", "Alternate Treaty Name", "Statute", "Land Cession Reference", "Tribes"])
df.to_csv("treaties.csv", index=True)