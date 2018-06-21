# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''

class UserRole(object):
    sql = "insert into `USER_ROLE`(USER_OID, ROLE_OID) values(%s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select USER_OID, ROLE_OID from `USER_ROLE`')
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
