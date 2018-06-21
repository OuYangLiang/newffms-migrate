# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import pymysql
import compute

oldConn = pymysql.connect(host='localhost', user='root', port=3306, password='password', db='newffms', charset='utf8')
newConn = pymysql.connect(host='localhost', user='root', port=3306, password='password', db='newffms2', charset='utf8')

audits = compute.getAccountAudit(oldConn)
incomings = compute.getIncomings(newConn)
consumptions = compute.getConsumptions(newConn)

alls = audits + incomings + consumptions

#print len(alls)

sortedList = sorted(alls, key = lambda item: item.getTime(), reverse=True)
 
for item in sortedList:
    item.doRecord(newConn)
    
sortedList2 = sorted(alls, key = lambda item: item.getTime(), reverse=False)
  
for item in sortedList2:
    item.doReal(newConn)