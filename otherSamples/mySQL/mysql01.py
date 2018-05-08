import pymysql
import time

def getDBVersion(myDB):
    getData = myDB.cursor()
    getData.execute('SELECT VERSION()')
    myData = getData.fetchone()
    print(myData)
    return

def getDBData(myDB, myEMail):
    getData = myDB.cursor()
    getData.execute("SELECT * FROM radius.voucherData where name = '" + myEMail + "'")
    myData = getData.fetchall()
    for n in myData:
        print(n)
    return

def connectMySQL():
    try:
        myDataBase = pymysql.connect("10.40.40.139","root","Laboratorio","radius" )
    except pymysql.err.OperationalError as error:
        print(error)
        time.sleep(5)
        return connectMySQL()
    else:
        print(f'Conectado Ok.')
        getDBVersion(myDataBase)
        EMail = 'joao.netto@actar.com.br'
        getDBData(myDataBase, EMail)
        myDataBase.close()
        return

if __name__ == '__main__':
    connectMySQL()



#exit()

#cursor = db.cursor()

#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print(data)

#db.close()
