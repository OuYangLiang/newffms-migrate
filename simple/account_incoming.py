# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateAccountIncoming(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select ACNT_OID, INCOMING_OID from `ACCOUNT_INCOMING`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `ACCOUNT_INCOMING`(ACNT_OID, INCOMING_OID) values(%s, %s)", item)
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
