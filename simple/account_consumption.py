# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateAccountConsumption(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select ACNT_OID, CPN_OID, AMOUNT from `ACCOUNT_CONSUMPTION`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `ACCOUNT_CONSUMPTION`(ACNT_OID, CPN_OID, AMOUNT) values(%s, %s, %s)", item)
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
