from datetime import datetime, date, time
import json

def myException(myEMail):
    with open('exceptionUser.json') as inFile:
        myData = json.load(inFile)

    for myJSon in myData.keys():
        if myEMail in myJSon:
            for myDayOfWeek in myData[myJSon].keys():
                if 'everyDay' in myDayOfWeek:
                    myResult = myData[myJSon][myDayOfWeek].split(',')
                elif datetime.now().strftime("%a") in myDayOfWeek:
                    myResult = myData[myJSon][myDayOfWeek].split(',')
                else:
                    myResult = False
            break
        else:
            myResult = False

    return myResult


def workingHours():
    myEMailWorking = "joao.rei@actar.com.br"
    myDateNow = datetime.now().timestamp()

    with open('workingHours.json') as inFile:
        myData = json.load(inFile)

    for myJSon in myData:
        if datetime.now().strftime("%a") in myJSon:
            myResult = myData[myJSon].split(',')
            myBgnDate = datetime.now().strftime("%d %b %y") + ' ' + myResult[0]
            myBgnDate = datetime.strptime(myBgnDate, '%d %b %y %H:%M:%S').timestamp()
            myEndDate = datetime.now().strftime("%d %b %y") + ' ' + myResult[1]
            myEndDate = datetime.strptime(myEndDate, '%d %b %y %H:%M:%S').timestamp()
            break
        else:
            myResult = False

    if myResult is False:
        print('Retornar False devido a Falta do dia de Semana. Autenticacao Reject')
        return False

    myJSonDate = myException(myEMailWorking)
    if myJSonDate is not False:
        myBgnDate = datetime.now().strftime("%d %b %y") + ' ' + myJSonDate[0]
        myBgnDate = datetime.strptime(myBgnDate, '%d %b %y %H:%M:%S').timestamp()
        myEndDate = datetime.now().strftime("%d %b %y") + ' ' + myJSonDate[1]
        myEndDate = datetime.strptime(myEndDate, '%d %b %y %H:%M:%S').timestamp()

    if myDateNow >= myBgnDate:
        print('A data/hora atual esta após o inicio do dia')
        if myDateNow <= myEndDate:
            print('A data/hora do Usuario esta antes do final do dia.')
            return myEndDate
        else:
            print('A data/hora do Usario esta após o esperado do final do dia.')
            return False
    else:
        print('A data/hora do usuário esta antes do esperado do inicio do dia.')
        return False

if __name__ == '__main__':



    myResult = workingHours()
    print(myResult)
