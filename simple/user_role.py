# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateUserRole(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select USER_OID, ROLE_OID from `USER_ROLE`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `USER_ROLE`(USER_OID, ROLE_OID) values(%s, %s)", item)
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
