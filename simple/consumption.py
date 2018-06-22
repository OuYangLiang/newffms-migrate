# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import uuid
def migrateConsumption(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select CPN_OID, CPN_TYPE, AMOUNT, CPN_TIME, CONFIRMED, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO from `CONSUMPTION`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `CONSUMPTION`(CPN_OID, CPN_TYPE, AMOUNT, CPN_TIME, BATCH_NUM, CONFIRMED, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [item[0], item[1], item[2], item[3], str(uuid.uuid4()).replace('-',''), item[4], item[5], item[6], item[7], item[8], item[9]])
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
