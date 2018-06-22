# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateOperationUrl(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select OPN_OID, OPN_URL from `OPERATION_URL`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `OPERATION_URL`(OPN_OID, OPN_URL) values(%s, %s)", [item[0], item[1]])
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
