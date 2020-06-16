import mysql.connector

class DBHelper:
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1", user="root", password="",database="tinder")
            self._mycursor=self._connection.cursor()
        except:
            print("Could not connect")

    def search(self, key1,value1,key2,value2,table):
        self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(table,key1,value1,key2,value2))
        response=self._mycursor.fetchall()

        return response

    def searchOne(self, key,value, table,type):
        self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` {} '{}'".format(table,key,type,value))
        response=self._mycursor.fetchall()

        return response

    def insert(self, inputDict, table):

        cols=""
        vals=""

        for i in inputDict:
            cols=cols + "`" + i + "`" + ","
            vals = vals + "'" + str(inputDict[i]) + "'" + ","

        cols=cols[:-1]
        vals=vals[:-1]
        try:
            self._mycursor.execute("INSERT INTO `{}` ({}) VALUES ({})".format(table,cols,vals))
            self._connection.commit()
            return 1
        except:
            return 0
