import json
from socket import *
import thread
import signal
import pickle
import time
import sys


def pp(a, b):
    while(1):
        text = raw_input()
        # text - is command from tornado
        try:
            parsed_json = json.loads(text)
        except:
            parsed_json = None

        # dummy button events - change color
        try:
            if parsed_json['onmousedown'] == 'START':
                sys.stdout.write('{"arg1": "path11108", "arg2": "fill", "arg3": "set_property", "arg4": "#ff0000"}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['click'] == 'circle11031':
                sys.stdout.write('{"arg1": "path11108", "arg2": "fill", "arg3": "set_property", "arg4": "#00ff00"}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['onmousedown'] == 'circle11035':
                sys.stdout.write('{"arg1": "path11108", "arg2": "fill", "arg3": "set_property", "arg4": "#0000ff"}\r\n')
                sys.stdout.flush()
        except:
            pass


# start listener thread
thread.start_new_thread(pp, (1, 2))
sys.stdout.write('{"machine": "started"}\r\n')
sys.stdout.flush()

# dummy action - blinky
for i in range(3):
    led_green = '{"arg1": "path11208", "arg2": "fill", "arg3": "set_property", "arg4": "#00ff00"}'
    led_red = '{"arg1": "path11208", "arg2": "fill", "arg3": "set_property", "arg4": "#ffffff"}'

    sys.stdout.write(led_green+"\r\n")
    sys.stdout.flush()
    time.sleep(0.5)

    sys.stdout.write(led_red+"\r\n")
    sys.stdout.flush()
    time.sleep(0.5)

# endless loop
while(1):
    time.sleep(1)

sys.stdout.write('{"machine": "ended"}\r\n')
sys.stdout.flush()
