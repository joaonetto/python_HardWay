from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

ip = get('http://10.0.1.6:3000').text
print('My public IP address is: {}'.format(ip))
