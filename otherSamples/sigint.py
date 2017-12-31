import signal
import sys

# learn more about Signal in:
# https://docs.python.org/dev/library/signal.html

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
