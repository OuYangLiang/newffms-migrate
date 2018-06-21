# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''

class Category(object):
    sql = "insert into `CATEGORY`(CATEGORY_OID, CATEGORY_DESC, MONTHLY_BUDGET, CATEGORY_LEVEL, IS_LEAF, PARENT_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select CATEGORY_OID, CATEGORY_DESC, MONTHLY_BUDGET, CATEGORY_LEVEL, IS_LEAF, PARENT_OID, CREATE_TIME, UPDATE_TIME, CREATE_BY, UPDATE_BY, SEQ_NO from `CATEGORY`')
        newCur = newConn.cursor()
        try:
            for item in oldCur.fetchall():
                newCur.execute(self.sql, [item[0], item[1], item[2], (item[3]+1), item[4], item[5], item[6], item[7], item[8], item[9], item[10] ])
            newConn.commit()
        except Exception:
            newConn.rollback()
            raise
        finally:
            oldCur.close()
            newCur.close()
