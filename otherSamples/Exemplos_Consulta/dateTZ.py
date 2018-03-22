#import datetime
import pytz
from datetime import datetime

def convertTZ(date2Convert, actualTZ):
    date2Convert = date2Convert.split()
    date2Convert.pop(2)
    date2Convert = datetime.strptime(str(date2Convert[0] + ' ' + date2Convert[1]), '%Y-%m-%d %H:%M:%S')
    if actualTZ != 'utc':
        from_timezone = pytz.timezone(actualTZ)
        to_timezone = pytz.timezone("utc")
        print(type(from_timezone))
        date2Convert = from_timezone.localize(date2Convert).astimezone(to_timezone)
    else:
        print('é utc')
    return date2Convert.timestamp()

if __name__ == '__main__':
    a = '2017-12-22 18:52:18 UTC'
    #a = '2017-12-22 18:52:18 BRST'
    b = 'utc'
    #b = 'America/Sao_Paulo'
    resultado = convertTZ(a,b)
    resultado = '1521582719.3652825'
    print("=" * 50)
    print(f'O valor de Epoch de {a} é:\n{resultado}')
    print("=" * 50)
    print(f"Convertendo de Epoch {resultado} para datetime: {datetime.fromtimestamp(float(resultado)).strftime('%Y-%m-%d %H:%M:%S')}")
