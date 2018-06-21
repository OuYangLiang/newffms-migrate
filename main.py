# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import pymysql
import simple


oldConn = pymysql.connect(host='localhost', user='root', port=3306, password='password123', db='newffms', charset='utf8')
newConn = pymysql.connect(host='localhost', user='root', port=3306, password='password123', db='newffms2', charset='utf8')

userType = simple.UserType()
userTypeOpn = simple.UserTypeOperation()
operation = simple.Operation()
operationUrl = simple.OperationUrl()
userProfile = simple.UserProfile()
roleProfile = simple.RoleProfile()
roleOperation = simple.RoleOperation()
module = simple.Module()
userRole = simple.UserRole()
category = simple.Category()
incoming = simple.Incoming()
accountIncoming = simple.AccountIncoming()
account = simple.Account()
cousumption = simple.Consumption()
consumptionItem = simple.ConsumptionItem()
accountConsumption= simple.AccountConsumption()
userType.migrate(newConn)
userTypeOpn.migrate(newConn)
operation.migrate(oldConn, newConn)
operationUrl.migrate(oldConn, newConn)
userProfile.migrate(oldConn, newConn)
roleProfile.migrate(oldConn, newConn)
roleOperation.migrate(oldConn, newConn)
module.migrate(oldConn, newConn)
userRole.migrate(oldConn, newConn)
category.migrate(oldConn, newConn)
incoming.migrate(oldConn, newConn)
accountIncoming.migrate(oldConn, newConn)
account.migrate(oldConn, newConn)
cousumption.migrate(oldConn, newConn)
consumptionItem.migrate(oldConn, newConn)
accountConsumption.migrate(oldConn, newConn)
newConn.close()