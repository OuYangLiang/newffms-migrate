'''
Created on Jun 21, 2018

@author: ouyang
'''
# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''

class Module(object):
    sql = "insert into `MODULE`(MODULE_OID, MODULE_DESC, MODULE_LEVEL, SHOW_ORDER, MODULE_LINK, PARENT_OID) values(%s, %s, %s, %s, %s, %s)"
    
    def migrate(self, oldConn, newConn):
        oldCur= oldConn.cursor()
        oldCur.execute('select MODULE_OID, MODULE_DESC, MODULE_LEVEL, SHOW_ORDER, MODULE_LINK, PARENT_OID from `MODULE`')
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
