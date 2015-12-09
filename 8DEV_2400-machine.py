import json
from socket import *
import thread
import signal
import pickle
import time
import sys


PIN = []

PIN['D0'] =  {"bubble1":"path5743", "text1":"text11311_13_", "bubble2":"path5750", "text2":"text11311_12_"}
PIN['D1'] =  {"bubble1":"path5757", "text1":"text11311_15_", "bubble2":"path5764", "text2":"text11311_14_"}
PIN['D2'] =  {"bubble1":"path5771", "text1":"text11311_17_", "bubble2":"path5778", "text2":"text11311_16_"}
PIN['D3'] =  {"bubble1":"path5785", "text1":"text11311_19_", "bubble2":"path5792", "text2":"text11311_18_"}
PIN['D4'] =  {"bubble1":"path5799", "text1":"text11311_21_", "bubble2":"path5806", "text2":"text11311_20_"}
PIN['D5'] =  {"bubble1":"path5813", "text1":"text11311_23_", "bubble2":"path5820", "text2":"text11311_22_"}
PIN['D6'] =  {"bubble1":"path5827", "text1":"text11311_25_", "bubble2":"path5834", "text2":"text11311_24_"}
PIN['D7'] =  {"bubble1":"path5841", "text1":"text11311_27_", "bubble2":"path5848", "text2":"text11311_26_"}
PIN['D8'] =  {"bubble1":"path5855", "text1":"text11311_29_", "bubble2":"path5862", "text2":"text11311_28_"}
PIN['D9'] =  {"bubble1":"path5869", "text1":"text11311_31_", "bubble2":"path5876", "text2":"text11311_30_"}
PIN['D10'] = {"bubble1":"path5883", "text1":"text11311_33_", "bubble2":"path5890", "text2":"text11311_32_"}
PIN['D11'] = {"bubble1":"path5897", "text1":"text11311_35_", "bubble2":"path5904", "text2":"text11311_34_"}
PIN['D12'] = {"bubble1":"path3030", "text1":"text11405", "bubble2":"path5736", "text2":"text11311_11_"}
PIN['D13'] = {"bubble1":"path3024", "text1":"text11399", "bubble2":"path5729", "text2":"text11311_10_"}
PIN['D14'] = {"bubble1":"path3018", "text1":"text11393", "bubble2":"path5722", "text2":"text11311_9_"}
PIN['D15'] = {"bubble1":"path3012", "text1":"text11387", "bubble2":"path5715", "text2":"text11311_8_"}
PIN['D16'] = {"bubble1":"path3006", "text1":"text11379", "bubble2":"path5708", "text2":"text11311_7_"}
PIN['D17'] = {"bubble1":"path3000", "text1":"text11375", "bubble2":"path5701", "text2":"text11311_6_"}
PIN['D18'] = {"bubble1":"path2994", "text1":"text11363", "bubble2":"path5694", "text2":"text11311_5_"}
PIN['D19'] = {"bubble1":"path2988", "text1":"text11347", "bubble2":"path5687", "text2":"text11311_4_"}
PIN['D20'] = {"bubble1":"path3036", "text1":"path3036", "bubble2":"path5680", "text2":"text11311_3_"}
PIN['D21'] = {"bubble1":"path3042", "text1":"text11321", "bubble2":"path5673", "text2":"text11311_2_"}
PIN['D22'] = {"bubble1":"path3048", "text1":"text11311", "bubble2":"path5666", "text2":"text11311_1_"}

PIN['BTN_1'] = {"btn":"circle11031"}
PIN["BTN_RST"] = {"btn":"circle11035"}

PIN['LED_1'] = {"led":"path11108"}
PIN['LED_PWR'] = {"led":"path11208"}


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
            if parsed_json['mousedown'] == 'START':
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
            if parsed_json['mousedown'] == 'circle11035':
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
    set_fill = '{"arg1": "%s", "arg2": "fill", "arg3": "set_property", "arg4": "%s"}'+"\r\n"

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

# endless loop
while(1):
    time.sleep(1)

sys.stdout.write('{"machine": "ended"}\r\n')
sys.stdout.flush()
