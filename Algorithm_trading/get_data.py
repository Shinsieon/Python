import  requests as re
from bs4 import BeautifulSoup
from pandas import DataFrame, Series
import numpy as np
import pandas as pd

tickers = {'005930':'삼성전자',
           '000660':'SK하이닉스',
          '005490':'POSCO',
          '034730':'SK',
          '105560':'KB금융',
          '035420':'NAVER',
          '055550':'신한지주',
          }

my_folder = "C:/Users/user/Desktop/stock"

def get_fnguide_table(tickers):

    for code in tickers.keys() :
        """경로탑색"""
        url = re.get('http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A%s' % (code))
        url = url.content
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
        fn_body = body.find('div',{'class':'fng_body asp_body'})
        ur_table = fn_body.find('div',{'id': 'div15'})
        table = ur_table.find('div',{'id':'highlight_D_Y'})

        tbody = table.find('tbody')

        tr = tbody.find_all('tr')
        Table = DataFrame()

        for i in tr:
            #항목 가져오기
            category = i.find('span',{'class':'txt_acd'})

            if category == None:
                category = i.find('th')
            category = category.text.strip()
            #값 가져오기
            value_list = []
            j = i.find_all('td',{'class','r'})

            for value in j:
                temp = value.text.replace(',','').strip()
                try:
                    tempt = float(temp)
                    value_list.append(temp)
                except:
                    value_list.append(0)
            Table['%s'%(category)] = value_list

            #기간 가져오기
            thead = table.find('thead')
            tr_2 = thead.find('tr',{'class','td_gapcolor2'}).find_all('th')
            year_list = []
            for i in tr_2:
                try:
                    temp_year = i.find('span', {'class','txt_acd'}).text
                except:
                    temp_year = i.text
                year_list.append(temp_year)
            Table.index = year_list
        Table = Table.T
        #Csv 파일로 저장
        Table.to_csv('%s/%s.csv'%(my_folder,tickers[code]))
    return
get_fnguide_table(tickers)



