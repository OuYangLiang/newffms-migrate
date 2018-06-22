# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateUserProfile(oldConn, newConn):
    oldCur= oldConn.cursor()
    oldCur.execute('select USER_OID, USER_NAME, USER_ALIAS, GENDER, PHONE, EMAIL, ICON, REMARKS, LOGIN_ID, LOGIN_PWD, USER_TYPE_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO from `USER_PROFILE`')
    newCur = newConn.cursor()
    try:
        for item in oldCur.fetchall():
            newCur.execute("insert into `USER_PROFILE`(USER_OID, USER_NAME, USER_ALIAS, GENDER, PHONE, EMAIL, ICON, REMARKS, LOGIN_ID, LOGIN_PWD, USER_TYPE_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15] ])
        newConn.commit()
    except Exception:
        newConn.rollback()
        raise
    finally:
        oldCur.close()
        newCur.close()
