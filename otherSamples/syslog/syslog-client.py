#!/usr/bin/env python

import argparse
import logging
import logging.handlers
import socket
from termcolor import colored
from termcolor import cprint
from sys import argv

myHostname = socket.gethostname()
myPy = argv[0]
parser = argparse.ArgumentParser(__file__,
                                 description="Gerador de mensagens de Syslog")

parser.add_argument("--ip",
                    "-ip",
                    default="10.0.1.6",
                    help="Informe o endereço IP para o servidor de Syslog")

parser.add_argument("--port",
                    "-p",
                    type=int,
                    default=514,
                    help="Informe a porta para o envio da mensagem. Default: 514")

parser.add_argument("--level",
                    "-l",
                    default="DEBUG",
                    help="Qual o nivel de mensagem para o Syslog. Default é DEBUG")

parser.add_argument("--message",
                    "-m",
                    required=True,
                    help="Qual a mensagem a ser enviada")


def string_to_level(log_level):
    """ Convert a commandline string to a proper log level
    @param string log_level     command line log level argument
    @return logging.LEVEL       the logging.LEVEL object to return
    """
    if log_level == "CRITICAL":
        return logging.CRITICAL
    if log_level == "ERROR":
        return logging.ERROR
    if log_level == "WARNING":
        return logging.WARNING
    if log_level == "INFO":
        return logging.INFO
    if log_level == "DEBUG":
        return logging.DEBUG
    return logging.NOTSET

if __name__ == "__main__":
    #args = parser.parse_args()
    #if args.message == None:
    #    pass
    #else:
    args = parser.parse_args()
    print(args)
    syslogger = logging.getLogger('SyslogLogger')
    syslogger.setLevel(string_to_level(args.level))
    handler = logging.handlers.SysLogHandler(address=(args.ip, args.port),
                                         facility=19)
    syslogger.addHandler(handler)
    syslogger.log(syslogger.level, '<'+args.level+'> <Conteiner=' + myHostname+ '> <pyProg='+myPy+'> ' + args.message)
