#!/usr/bin/python3
import cx_Oracle as db


class SqlHelper:

    def __init__(this):
        pass

    @staticmethod
    def connectOracle(connStr):
        # # dsn:data source name
        # dsn = db.makedsn(ORACLE_HOST, ORACLE_PORT, ORACLE_SID)
        # con = db.connect(ORACLE_USER, ORACLE_PASSWORD, dsn)
        conn = db.connect(connStr)    # 用户密码主机端口SID
        return conn

    def query(conn, sqlStr):
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        print("\n>>> "+sqlStr.rstrip('\n'))
        cursor.execute(sqlStr)
        columNames = [d[0] for d in cursor.description]
        # resList = []
        rows = cursor.fetchall()
        # obselete output : dict(key-value)
        # for row in rows:
        #     resList.append(dict(zip(columNames, row)))
        cursor.close()
        return [columNames, rows]

    def queryByDcit(conn, sqlStr):
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sqlStr)
        print("\n>>> "+sqlStr)
        columNames = [d[0] for d in cursor.description]
        print(columNames)
        resList = []
        rows = cursor.fetchall()
        # obselete output : dict(key-value)
        for row in rows:
            resList.append(dict(zip(columNames, row)))
        cursor.close()
        return resList

    # todo support for thread pools and Exceute methods
