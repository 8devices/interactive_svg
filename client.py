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
            if parsed_json['mouseout'] == 'polygon10753':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "polygon10753", "style": {"fill": "#1E1E1E"}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['mouseover'] == 'polygon10753':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "polygon10753", "style": {"fill": "#8888FF"}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['click'] == 'circle11031':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "path11108", "style": {"fill": "#ff0000"}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['mousedown'] == 'circle11035':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "path11108", "style": {"fill": "#0000ff"}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['click'] == 'btn-green-pcb':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "path7334", "style": {"fill": "#118811"}}\r\n')
                sys.stdout.write('{"svgId": "svg_img", "elmId": "rect7328", "style": {"fill": "#006600"}, "attrSet": {"stroke":""}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['click'] == 'btn-blue-pcb':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "path7334", "style": {"fill": "#496FA5"}}\r\n')
                sys.stdout.write('{"svgId": "svg_img", "elmId": "rect7328", "style": {"fill": "#285199"}, "attrSet": {"stroke":""}}\r\n')
                sys.stdout.flush()
        except:
            pass

        try:
            if parsed_json['click'] == 'btn-red-pcb':
                sys.stdout.write('{"svgId": "svg_img", "elmId": "path7334", "style": {"fill": "#AA2222"}}\r\n')
                sys.stdout.write('{"svgId": "svg_img", "elmId": "rect7328", "style": {"fill": "#770000"}, "attrSet":{"stroke":"#F00"}}\r\n')
                sys.stdout.flush()
        except:
            pass


# start listener thread
thread.start_new_thread(pp, (1, 2))
sys.stdout.write('{"machine": "started"}\r\n')
sys.stdout.flush()

# dummy action - blinky
for i in range(3):
    #set_fill = '{"arg1": "%s", "arg2": "fill", "arg3": "set_property", "arg4": "%s"}'+"\r\n"
    set_fill = '{"svgId": "svg_img", "elmId": "%s", "style": {"fill": "%s"}}'+"\r\n"

    led_d16 = "path11108"
    led_pwr = "path11208"

    color_green = "#00ff00"
    color_white = "#ffffff"

    sys.stdout.write( str((set_fill) % (led_pwr, color_white )) )
    sys.stdout.write( str((set_fill) % (led_d16, color_green )) )
    sys.stdout.flush()
    time.sleep(0.5)

    sys.stdout.write( str((set_fill) % (led_pwr, color_green )) )
    sys.stdout.write( str((set_fill) % (led_d16, color_white )) )
    sys.stdout.flush()
    time.sleep(0.5)

sys.stdout.write('{"svgId": "svg_img", "elmId": "circle11031", "eventAdd": "click" }\r\n')
sys.stdout.write('{"svgId": "svg_img", "elmId": "circle11035", "eventAdd": "mousedown" }\r\n')
sys.stdout.write('{"svgId": "svg_img", "elmId": "polygon10753", "eventAdd": "mouseover" }\r\n')
sys.stdout.write('{"svgId": "svg_img", "elmId": "polygon10753", "eventAdd": "mouseout" }\r\n')

# Adds events to buttons and sets attribute disabled to empty 
sys.stdout.write('{"elmId": "btn-green-pcb", "eventAdd": "click", "attrRem": {"disabled":""}}\r\n')
sys.stdout.write('{"elmId": "btn-blue-pcb", "eventAdd": "click", "attrRem": {"disabled":""}}\r\n')
sys.stdout.write('{"elmId": "btn-red-pcb", "eventAdd": "click", "attrRem": {"disabled":""}, "attrSet": { "class": ["one","two","three"] }}\r\n')
sys.stdout.write('{"elmId": "btn-test", "eventAdd": "click", "attrRem": {"disabled":""}, "attrRem": { "class": "" }}\r\n')
sys.stdout.flush()

# endless loop
while(1):
    time.sleep(1)

sys.stdout.write('{"machine": "ended"}\r\n')
sys.stdout.flush()
