import sys
from math import cos, radians

for i in range(360):
	print(cos(radians(i)))
import pandas as pd
import datetime as dt
import numpy as np
#import json
#from pprint import pprint
#from bs4 import BeautifulSoup
#import time
#from selenium import webdriver

##**automatisiertes Crawlen von GA-Seite --> Schwierigkeit beim Einloggen
##register chrome as standard browser and containing Google-Analytics-login-data
##browser = webdriver.Chrome(r'C:\Users\tungnguyen\Python\chromedriver_win32\chromedriver.exe')
## def gethtmlfromurl(url):  
##     link=deletespaces(''.join(['window.open(',url,');']))
##     print(link)
##     browser.execute_script(link)
##     return True
#def deletespaces(u):
#    return u.replace(" ","")

##import Käuferliste
#file = r'C:\Users\tungnguyen\Python\Terrafinanz\Käuferliste.xlsx'
#xl = pd.ExcelFile(file)
#df1 = xl.parse('Käuferliste',header=0).iloc[:4152]
#df1 = df1.fillna("")
##import GA-Client-ID with firt/last name
#with open('2019-01-17-inquiries.1000.json') as inquirylist:
#    inquiries = json.load(inquirylist)
##find name of buyer from Käuferliste in GA-Client-ID
## for column in df1:
##     print(column," type:",type(column))
#withID,withoutID=0,0
#for client in range(len(df1)):
#    for buyer in range(len(inquiries)):
#        if (deletespaces(inquiries[buyer]['lastname'])==deletespaces(df1['Nachname'][client])): #(inquiries[buyer]['firstname']==df1['Vorname'][client])
#            if (deletespaces(inquiries[buyer]['firstname']) in deletespaces(df1['Vorname'][client])):
#                print("**",inquiries[buyer]['lastname'].center(12," "), "buyer: ",df1['Vorname'][client].center(12," ")," - ",inquiries[buyer]['firstname']," :inquiry")
#                print("Datum Notar: ",str(df1['Notartermin'][client])[:10], "; Datum Anfrage: ",inquiries[buyer]['created'][:10]) #," Objekt:",df1['Objektitel'][buyer])
#                print("CRM-EnquiryId: ",inquiries[buyer]['crmEnquiryId'])
#                if 'cookieGoogleAnalytics' in inquiries[buyer]:
#                    fullID=inquiries[buyer]['cookieGoogleAnalytics']
#                    shortID=fullID[-(len(fullID)-6):]
#                    print(shortID,' -- GA Client-ID')
#                    withID+=1
#                    link=''.join(['https://analytics.google.com/analytics/web/?utm_campaign=SuiteHeader&utm_source=UniversalPicker&utm_medium=getStarted#/report/visitors-user-activity/a3119893w5828897p6017904/_u.date00=20180101&_u.date01=20190116&_.useg=builtin1&_r.userId=',shortID ,'&_r.userListReportStates=%3F_u.date00=20180101%2526_u.date01=20190116%2526_.useg=builtin1%2526explorer-table-dataTable.sortColumnName=analytics.transactionRevenue%2526explorer-table-dataTable.sortDescending=true%2526explorer-table.plotKeys=%5B%5D%2526explorer-table.rowCount=5000%2526explorer-table.filter=',shortID,'&_r.userListReportId=visitors-legacy-user-id/'])
#                    print(deletespaces(link))
#                else:
#                    withoutID+=1
##             else: 
##                 print("  ",inquiries[buyer]['lastname'].center(12," "), "buyer: ",df1['Vorname'][client].center(12," ")," - ",inquiries[buyer]['firstname']," :inquiry".rjust(40," "))
#print('Es gibt ',withID,' Anfragen mit Client-ID und ',withoutID,' Anfragen ohne Client-ID')
