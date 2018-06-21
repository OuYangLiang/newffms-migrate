# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
class Account(object):
    sql = "insert into `ACCOUNT`(ACNT_OID, ACNT_DESC, ACNT_TYPE, BALANCE, QUOTA, DEBT, OWNER_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select ACNT_OID, ACNT_DESC, ACNT_TYPE, BALANCE, QUOTA, DEBT, OWNER_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO from `ACCOUNT`')
        newCur = newConn.cursor()
        try:
            for item in oldCur.fetchall():
                newCur.execute(self.sql, item)
            newConn.commit()
        except Exception:
            newConn.rollback()
            raise
        finally:
            oldCur.close()
            newCur.close()
