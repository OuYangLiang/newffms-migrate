# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import time
import account
import uuid
class AccountAudit(object):
    def __init__(self, conn, adtOid, adtDesc, adtType, adtTime, amount, acntOid, refAcntOid, incomingOid, cpnOid, createTime, createBy):
        self.adtOid = adtOid
        self.adtDesc = adtDesc
        self.adtType = adtType
        self.adtTime = adtTime
        self.amount = amount
        self.acntOid = acntOid
        self.refAcntOid = refAcntOid
        self.incomingOid = incomingOid
        self.cpnOid = cpnOid
        self.createTime = createTime
        self.createBy = createBy
        
    def getTime(self):
        return time.mktime(self.adtTime.timetuple())
    
    def doRecord(self, conn):
        acnt = account.getAccount(conn, self.acntOid)
        acnt.inc(conn, self.amount)
        refacnt = account.getAccount(conn, self.refAcntOid)
        refacnt.sub(conn, self.amount)
        
    def doReal(self, conn):
        acnt = account.getAccount(conn, self.acntOid)
        refacnt = account.getAccount(conn, self.refAcntOid)
        
        acnt.sub(conn, self.amount)
        batch = str(uuid.uuid4()).replace('-','')
        insertAudit(conn, ['转账至：' + refacnt.acntDesc, 'Trans_subtract', self.adtTime, acnt.balance, self.amount, acnt.acntOid, batch, self.adtTime, self.createBy])
        
        refacnt.inc(conn, self.amount)
        insertAudit(conn, ['进账自：' + acnt.acntDesc, 'Trans_add', self.adtTime, refacnt.balance, self.amount, refacnt.acntOid, batch, self.adtTime, self.createBy])
    
def getAccountAudit(conn):
    try:
        cursor= conn.cursor()
        cursor.execute("select ADT_OID, ADT_DESC, ADT_TYPE, ADT_TIME, AMOUNT, ACNT_OID, REF_ACNT_OID, INCOMING_OID, CPN_OID, CREATE_TIME, CREATE_BY from `ACCOUNT_AUDIT` where REF_ACNT_OID IS NOT NULL and ADT_TYPE = 'Subtract' order by ADT_OID desc")
        rlt = []
        for item in cursor.fetchall():
            rlt.append(AccountAudit(conn, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]))
            
        return rlt
    finally:
        cursor.close()
        
def insertAudit(conn, audit):
    try:
        cursor = conn.cursor()
        cursor.execute("insert into ACCOUNT_AUDIT(ADT_DESC, ADT_TYPE, ADT_TIME, BALANCE_AFTER, CHG_AMT, ACNT_OID, BATCH_NUM, CREATE_TIME, CREATE_BY) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", audit)
    finally:
        cursor.close()