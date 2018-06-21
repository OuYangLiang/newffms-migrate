# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import time
import account
import account_audit
class Consumption(object):
    def __init__(self, conn, cpnOid, cpnType, amount, cpnTime, batchNum, createBy):
        self.cpnOid = cpnOid
        self.cpnType = cpnType
        self.amount = amount
        self.cpnTime = cpnTime
        self.batchNum = batchNum
        self.createBy = createBy
        self.itemDescs = []
        self.account = []
        try:
            cursor= conn.cursor()
            cursor.execute('select ITEM_DESC from CONSUMPTION_ITEM WHERE CPN_OID = %s', self.cpnOid)
            for item in cursor.fetchall():
                self.itemDescs.append(item[0])
        finally:
            cursor.close()
              
        try:
            cursor= conn.cursor()
            cursor.execute('select ACNT_OID, AMOUNT from ACCOUNT_CONSUMPTION WHERE CPN_OID = %s', self.cpnOid)
            for item in cursor.fetchall():
                self.account.append(item)
        finally:
            cursor.close()
    
    def getTime(self):
        return time.mktime(self.cpnTime.timetuple())
    
    def doRecord(self, conn):
        for item in self.account:
            acnt = account.getAccount(conn, item[0])
            acnt.inc(conn, self.amount)
            
    def doReal(self, conn):
        for item in self.account:
            acnt = account.getAccount(conn, item[0])
            acnt.sub(conn, item[1])
            account_audit.insertAudit(conn, [self.itemDescs, 'Subtract', self.cpnTime, acnt.balance, item[1], item[0], self.batchNum, self.cpnTime, self.createBy])
        
def getConsumptions(conn):
    try:
        cursor= conn.cursor()
        cursor.execute('select CPN_OID, CPN_TYPE, AMOUNT, CPN_TIME, BATCH_NUM, CREATE_BY from `CONSUMPTION` order by CPN_TIME desc, CPN_OID desc')
        consumptionList = []
        for item in cursor.fetchall():
            consumptionList.append(Consumption(conn, item[0], item[1], item[2], item[3], item[4], item[5]))
            
        return consumptionList
    finally:
        cursor.close()







