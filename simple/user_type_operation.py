# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateUserTypeOperation(conn):
    cursor = conn.cursor()
    try:
        for x in range(1,29):
            cursor.execute("insert into `USER_TYPE_OPERATION`(USER_TYPE_OID, OPN_OID) values(%s, %s)", [1, x])
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
