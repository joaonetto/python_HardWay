import sys
from termcolor import colored
from termcolor import cprint

def showArgv():
    # Cabecalho
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Interface_Get'), 'yellow', attrs=['bold'], end='')
    cprint('* ', 'white', attrs=['bold'])
    # Apresenta Argumentos
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Argumentos:'), 'cyan', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -ip
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-ip', 'magenta', attrs=['bold'], end='')
    cprint(' - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Informe o IP do Device'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -i
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-i', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Informe qual interface para Coleta.'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -p
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-p', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Apresenta resultado na Console em formato JSON.'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -s
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-s', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format("Salva arquivo 'interface_get.json' para consulta."), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    # Apresenta Utilizacao
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Utilizacao:'), 'blue', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa a utilizacao
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\tinterface_get', 'cyan', attrs=['bold'], end='')
    cprint('  -ip ', 'magenta', attrs=['bold'], end='')
    cprint('<device_ip_address>', 'yellow', attrs=['bold'], end='')
    cprint(' -i ', 'magenta', attrs=['bold'], end='')
    cprint('<interface_name>', 'yellow', attrs=['bold'], end='')
    cprint(' -p ', 'magenta', attrs=['bold'], end='')
    cprint(' -s ', 'magenta', attrs=['bold'], end='')
    cprint('{:>6}'.format("*"), 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    # Apresenta Observacao
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Observacao:'), 'blue', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa a Observacao
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-> Na falta do argumento', 'white', attrs=['bold'], end='')
    cprint(' <device_ip_address> ', 'yellow', attrs=['bold'], end='')
    cprint('todo o processo sera', 'white', attrs=['bold'], end='')
    cprint('{:>7}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t   abortado.', 'white', attrs=['bold'], end='')
    cprint('{:>60}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('{:>79}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-> Na falta do argumento', 'white', attrs=['bold'], end='')
    cprint(' <interface_name> ', 'yellow', attrs=['bold'], end='')
    cprint('todas as interfaces serao', 'white', attrs=['bold'], end='')
    cprint('{:>5}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t   coletadas.', 'white', attrs=['bold'], end='')
    cprint('{:>59}'.format("*"), 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)

showArgv()


"""
In [8]: print('{:^30}'.format('center'))
            center

In [9]: print('{:<30}'.format('center'))
center

In [10]: print('{:>30}'.format('center'))
                        center
"""
