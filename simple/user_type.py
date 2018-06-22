# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
def migrateUserType(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("insert into `USER_TYPE`(USER_TYPE_OID, USER_TYPE_DESC) values(%s, %s)", [1, '普通用户'])
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        