import urllib.request  as urllib2

import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

import pandas as pd

import xlsxwriter

from openpyxl.reader.excel import load_workbook


"DB, Instance and Snap Id infomration collection class"
class Env():
    dbdf = pd.DataFrame()
    instancedf = pd.DataFrame()
    snapdf =  pd.DataFrame()

    def __init__ (self):
        "Constructor"
        print ("\nEtracting DB, Host and Snap details\n")

    def toexcel (sheet):
        with pd.ExcelWriter('output.xlsx') as writer:
            Env.dbdf.to_excel(writer, sheet_name=sheet,index=False)
            Env.instancedf.to_excel(writer, sheet_name=sheet,startrow = 5,index = False)
            Env.snapdf.to_excel(writer, sheet_name=sheet,startrow = 8,index = False)
        writer.save()

    "This function to calculate and dataframe "
    def calsdataframe(soup,table):
        rows=[]
        colNames = []

        for row in table.find_all("tr"):
            cells = row.find_all('th')
            for val in cells:
                colNames.append (val.find(text = True))

        for row in table.find_all("tr"):
            cells = row.find_all('td')
            for val in cells:
                rows.append (val.find(text=True))

        df = pd.DataFrame(rows,colNames)
        df = df.transpose()
        return df

    "This function is what called in main class of this application"
    def extractenvinfo (self,soup):
        rows=[]
        colNames = []
        dbTable = soup.find('table', summary='This table displays database instance information')
        Env.dbdf = Env.calsdataframe (soup,dbTable)
        instanceInfoTable=soup.find('table', summary='This table displays host information')
        Env.instancedf = Env.calsdataframe (soup,instanceInfoTable)
        snapInfoTable=soup.find('table', summary='This table displays snapshot information')
        Env.snapcal(snapInfoTable)
        Env.toexcel("EnvInfo")

    "This function to calculate SPAN Id information"
    def snapcal (table):
        a=[]
        b=[]
        cols = []

        for row in table.find_all("tr"):
            cells = row.find_all('th')
            for val in cells:
                if val.find(text = True) == "Snap Id" or val.find(text = True) == "Snap Time" or \
                    val.find(text = True) == "Sessions" or val.find(text = True) == ("Cursors/Session") or \
                    val.find(text = True) == "Instances":
                    cols.append (val.find(text = True))

        count=0
        rows=[]
        for row in table.find_all("tr"):
            if count < 3:
                cells = row.find_all('td')
                for val in cells:
                    if val.find(text = True) != "Begin Snap:" or val.find(text = True) != "End Snap:":
                        rows.append (val.find(text=True))
            count=count+1

        rows.remove('Begin Snap:')
        rows.remove('End Snap:')
        length = len(rows)
        middle_index = length//2
        a = rows[:middle_index]
        b = rows[middle_index:]
        data = pd.DataFrame(cols)
        data[1] = a
        data[2] = b
        Env.snapdf = data.transpose()
        Env.snapdf.columns=cols
        Env.snapdf = Env.snapdf.iloc[1:]