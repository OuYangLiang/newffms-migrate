# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''

class RoleOperation(object):
    sql = "insert into `ROLE_OPERATION`(ROLE_OID, OPN_OID) values(%s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select ROLE_OID, OPN_OID from `ROLE_OPERATION`')
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
