# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import time
import account
import account_audit
class Incoming(object):
    def __init__(self, conn, incomingOid, incomingDesc, amount, incomingType, ownerOid, incomingDate, batchNum, createBy):
        self.incomingOid = incomingOid
        self.incomingDesc = incomingDesc
        self.amount = amount
        self.incomingType = incomingType
        self.ownerOid = ownerOid
        self.incomingDate = incomingDate
        self.batchNum = batchNum
        self.createBy = createBy
        try:
            cursor= conn.cursor()
            cursor.execute('select ACNT_OID from ACCOUNT_INCOMING WHERE INCOMING_OID = %s', self.incomingOid)
            result = cursor.fetchone()
            self.acntOid = result[0]
        finally:
            cursor.close()
            
    def getTime(self):
        return time.mktime(self.incomingDate.timetuple())
        
    def doRecord(self, conn):
        acnt = account.getAccount(conn, self.acntOid)
        acnt.sub(conn, self.amount)
        
    def doReal(self, conn):
        acnt = account.getAccount(conn, self.acntOid)
        acnt.inc(conn, self.amount)
        account_audit.insertAudit(conn, [self.incomingDesc, 'Add', self.cpnTime, acnt.balance, self.amount, self.acntOid, self.batchNum, self.cpnTime, self.createBy])
        
def getIncomings(conn):
    try:
        cursor= conn.cursor()
        cursor.execute('select INCOMING_OID, INCOMING_DESC, AMOUNT, INCOMING_TYPE, OWNER_OID, INCOMING_DATE, BATCH_NUM, CREATE_BY from `INCOMING` order by INCOMING_DATE desc, INCOMING_OID desc')
        incomingList = []
        for item in cursor.fetchall():
            incomingList.append(Incoming(conn, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
            
        return incomingList
    finally:
        cursor.close()







