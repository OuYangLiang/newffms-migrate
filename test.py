# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import pymysql
import compute

newConn = pymysql.connect(host='localhost', user='root', port=3306, password='password123', db='newffms2', charset='utf8')

list1 = compute.getIncomings(newConn)
print len(list1);

list2 = compute.getConsumptions(newConn)
print len(list2);

list4 = list1 + list2

print len(list4)

list3 = sorted(list4, key = lambda item: item.getTime(), reverse=True)

for item in list3:
    item.doRecord(newConn)

# for i in range(1000):
#     if isinstance(list3[i], Consumption):
#         print '消费：', list3[i].cpnOid, list3[i].cpnTime, list3[i].itemDescs, list3[i].getTime()
#     else:
#         print '收入：', list3[i].incomingOid, list3[i].incomingDate, list3[i].incomingDesc, list3[i].getTime()

    
