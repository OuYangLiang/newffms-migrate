# encoding: utf-8
'''
Created on Jun 21, 2018

@author: ouyang
'''
import pymysql
import simple
import compute
import os

def transfer(oldConn, newConn):
    simple.migrateUserType(newConn)
    simple.migrateUserTypeOperation(newConn)
    simple.migrateOperation(oldConn, newConn)
    simple.migrateOperationUrl(oldConn, newConn)
    simple.migrateUserProfile(oldConn, newConn)
    simple.migrateRoleProfile(oldConn, newConn)
    simple.migrateRoleOperation(oldConn, newConn)
    simple.migrateModule(oldConn, newConn)
    simple.migrateUserRole(oldConn, newConn)
    simple.migrateCategory(oldConn, newConn)
    simple.migrateIncoming(oldConn, newConn)
    simple.migrateAccountIncoming(oldConn, newConn)
    simple.migrateAccount(oldConn, newConn)
    simple.migrateConsumption(oldConn, newConn)
    simple.migrateConsumptionItem(oldConn, newConn)
    simple.migrateAccountConsumption(oldConn, newConn)
    
def computeDetail(oldConn, newConn):
    audits = compute.getAccountAudit(oldConn)
    incomings = compute.getIncomings(newConn)
    consumptions = compute.getConsumptions(newConn)
    alls = audits + incomings + consumptions
    
    for item in alls:
        item.doRecord(newConn)
        
    sortedList = sorted(alls, key = lambda item: item.getTime(), reverse=False)
   
    for item in sortedList:
        item.doReal(newConn)

username    = 'root'
password    ='password123'
oldDBname   = 'newffms'
newDBname   = 'newffms2'
mysqlPath   = '/usr/local/mysql/bin/mysql'
initSqlPath = '/Users/ouyang/Documents/git_repos/newffms2/document/sql/'

print "Start to drop exist database [" + newDBname + "] ..."
os.system("bash ./drop-db.sh " + mysqlPath + " " + initSqlPath + " " + username + " " + password + " " + newDBname)

print "create a new database [" + newDBname + "] ..."
os.system("bash ./create-db.sh " + mysqlPath + " " + initSqlPath + " " + username + " " + password + " " + newDBname)

print "Start to create initial data ..."
os.system("bash ./init-db.sh " + mysqlPath + " " + initSqlPath + " " + username + " " + password + " " + newDBname)
print "Initial data created successfully ..."

oldConn = pymysql.connect(host='localhost', user=username, port=3306, password=password, db=oldDBname, charset='utf8')
newConn = pymysql.connect(host='localhost', user=username, port=3306, password=password, db=newDBname, charset='utf8')

try:
    print "Start to transfer data ..."
    transfer(oldConn, newConn)
    print "Data transfered successfully..."
    
    print "Start to compute account detail..."
    computeDetail(oldConn, newConn)
    print "Account detail computed successfully..."
    
finally:
    oldConn.close()
    newConn.close()