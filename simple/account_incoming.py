# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
class AccountIncoming(object):
    sql = "insert into `ACCOUNT_INCOMING`(ACNT_OID, INCOMING_OID) values(%s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select ACNT_OID, INCOMING_OID from `ACCOUNT_INCOMING`')
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
