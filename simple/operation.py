# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateOperation(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select OPN_OID, OPN_DESC, MODULE_OID from `OPERATION`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `OPERATION`(OPN_OID, OPN_DESC, MODULE_OID) values(%s, %s, %s)", [item[0], item[1], item[2] ])
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
