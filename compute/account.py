# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
class Account(object):
    def __init__(self, conn, acntOid, acntDesc, acntType, balance, debt):
        self.acntOid = acntOid
        self.acntDesc = acntDesc
        self.acntType = acntType
        self.balance = balance
        self.debt = debt
        
    def sub(self, conn, amt):
        self.balance = self.balance - amt;
        try:
            cursor= conn.cursor()
            cursor.execute('update `ACCOUNT` set BALANCE = %s where ACNT_OID = %s', [self.balance, self.acntOid])
            conn.commit()
        finally:
            cursor.close()
            
    def inc(self, conn, amt):
        self.balance = self.balance + amt;
        try:
            cursor= conn.cursor()
            cursor.execute('update `ACCOUNT` set BALANCE = %s where ACNT_OID = %s', [self.balance, self.acntOid])
            conn.commit()
        finally:
            cursor.close()
        
        
def getAccount(conn, acntOid):
    try:
        cursor= conn.cursor()
        cursor.execute('select ACNT_OID, ACNT_DESC, ACNT_TYPE, BALANCE, DEBT from `ACCOUNT` where ACNT_OID = %s', acntOid)
        result = cursor.fetchone()
        
        return Account(conn, result[0], result[1], result[2], result[3], result[4])
    finally:
        cursor.close()
