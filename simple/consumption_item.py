# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
class ConsumptionItem(object):
    sql = "insert into `CONSUMPTION_ITEM`(ITEM_OID, ITEM_DESC, AMOUNT, OWNER_OID, CPN_OID, CATEGORY_OID) values(%s, %s, %s, %s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select ITEM_OID, ITEM_DESC, AMOUNT, OWNER_OID, CPN_OID, CATEGORY_OID from `CONSUMPTION_ITEM`')
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
