#!/bin/bash

$1 -u $3 -p$4 $5 < ${2}1_create_tables.sql
$1 -u $3 -p$4 $5 < ${2}3_keys.sql

$1 -u $3 -p$4 <<EOF
    use $5;
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(9, '/report/queryUserAmtConsumption');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(9, '/report/queryUserRatioConsumption');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(9, '/report/queryCategoryRatioConsumption');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(9, '/report/queryDetailConsumption');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(17, '/report/queryTotalIncoming');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(17, '/report/queryTotalIncomingByType');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(17, '/report/queryIncomingByMonth');
    INSERT INTO OPERATION_URL(OPN_OID, OPN_URL) VALUES(18, '/account/alaxGetAllAccountsByUser');
EOF