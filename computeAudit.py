# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import pymysql
import compute

oldConn = pymysql.connect(host='localhost', user='root', port=3306, password='password123', db='newffms', charset='utf8')
newConn = pymysql.connect(host='localhost', user='root', port=3306, password='password123', db='newffms2', charset='utf8')

audits = compute.getAccountAudit(oldConn)
incomings = compute.getIncomings(newConn)
consumptions = compute.getConsumptions(newConn)

alls = audits + incomings + consumptions

for item in alls:
    item.doRecord(newConn)
    
sortedList = sorted(alls, key = lambda item: item.getTime(), reverse=True)
  
for item in sortedList:
    item.doReal(newConn)