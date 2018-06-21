# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''

class RoleProfile(object):
    sql = "insert into `ROLE_PROFILE`(ROLE_OID, ROLE_DESC, USER_TYPE_OID) values(%s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select ROLE_OID, ROLE_DESC, USER_TYPE_OID from `ROLE_PROFILE`')
        newCur = newConn.cursor()
        try:
            for item in oldCur.fetchall():
                newCur.execute(self.sql, [item[0], item[1], item[2] ])
            newConn.commit()
        except Exception:
            newConn.rollback()
            raise
        finally:
            oldCur.close()
            newCur.close()
