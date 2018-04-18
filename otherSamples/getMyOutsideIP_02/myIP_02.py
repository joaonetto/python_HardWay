from ipify import get_ip
from ipify.exceptions import ConnectionError, ServiceError

try:
    ip = get_ip()
except ConnectionError:
    # If you get here, it means you were unable to reach the ipify service,
    # most likely because of a network error on your end.
    print('Não consigo acessar o servico IPIFY.org')
except ServiceError:
    # If you get here, it means ipify is having issues, so the request
    # couldn't be completed :(
    print('O serviço IPIFY.org apresenta problemas.')
except:
    # Something else happened (non-ipify related). Maybe you hit CTRL-C
    # while the program was running, the kernel is killing your process, or
    # something else all together.
    print('Execução IPIFY.org cancelada.')

print(f'Meu IP externo é: {ip}')
