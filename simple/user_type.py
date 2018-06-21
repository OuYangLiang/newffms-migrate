# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
class UserType(object):
    sql = "insert into `USER_TYPE`(USER_TYPE_OID, USER_TYPE_DESC) values(%s, %s)"
    
    def migrate(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute(self.sql, [1, '普通用户'])
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
        