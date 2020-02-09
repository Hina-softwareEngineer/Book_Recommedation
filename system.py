import json
import numpy as np
import pandas as pd
import requests
import bs4

res=requests.get('https://www.kaggle.com/zygmunt/goodbooks-10k#books.csv')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
table = soup.find('table',{'class':'DataTable_Table-sc-rjxc30 gMUozE'})

rows = table.find_all('tr')
for row in rows:
    data = row.find_all('td')
    for cell in data:
        print(data[0].text)
# isbn=soup.find_all("DataTable_Cell-sc-1d2l9ix DataTable_RowCell-sc-3t2nmu DataTable_RowDataCell-sc-1tgr3mb bveFgu")
# print(isbn)
# List of all links



# body > main > div > div.site-layout__main-content > div > div > div > div > div.Home_Wrapper-sc-1lm6bf2.ePXBVM > div:nth-child(3) > div > div > div.DataExplorerPreview_Container-sc-1vxrlio.kdBYqj > div > div.content-box__content-section > div > table > tbody > tr:nth-child(1) > td.DataTable_Cell-sc-1d2l9ix.DataTable_RowCell-sc-3t2nmu.DataTable_RowDataCell-sc-1tgr3mb.bveFgu
# Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list


# for my_tag in soup.find_all(class_="DataTable_Cell-sc-1d2l9ix DataTable_TableCell-sc-13l0208 loOctw"):
#     print(my_tag.text)
# isbn=soup.find_all("td",class_='DataTable_Cell-sc-1d2l9ix DataTable_TableCell-sc-13l0208 loOctw')
#
# for n in isbn:
#     print(n)