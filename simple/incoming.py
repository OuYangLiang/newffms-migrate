# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import uuid
class Incoming(object):
    sql = "insert into `INCOMING`(INCOMING_OID, INCOMING_DESC, AMOUNT, INCOMING_TYPE, CONFIRMED, OWNER_OID, INCOMING_DATE, BATCH_NUM, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select INCOMING_OID, INCOMING_DESC, AMOUNT, INCOMING_TYPE, CONFIRMED, OWNER_OID, INCOMING_DATE, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO from `INCOMING`')
        newCur = newConn.cursor()
        try:
            for item in oldCur.fetchall():
                newCur.execute(self.sql, [item[0], item[1], item[2], item[3], item[4], item[5], item[6], str(uuid.uuid4()).replace('-',''), item[7], item[8], item[9], item[10], item[11] ])
            newConn.commit()
        except Exception:
            newConn.rollback()
            raise
        finally:
            oldCur.close()
            newCur.close()
