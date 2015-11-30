# -*- coding: utf-8 -*-

import tornado
from tornado import websocket, web, ioloop, iostream, tcpserver, gen
from tornado.options import define, options
import json
#import simplejson as json
import socket
import thread
import threading
import signal
import uuid
import subprocess
import time
import sys
import logging
#import pickle
#import shlex


sessions = {} # list of sessions (cookie, websocket, pipe)

# ------------------------------
# Nicely handle exit with CTRL+C
# ------------------------------
is_closing = False


def signal_handler(signum, frame):
    global is_closing
    is_closing = True

def try_exit():
    global is_closing
    if is_closing:
        ioloop.IOLoop.instance().stop()

def pipe_thread(cmd, cookie):
    global sessions
    bp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=None)
    session={}
    session = sessions[cookie]
    session["pipe"] = bp
    sessions[cookie] = session

    for line in iter(bp.stdout.readline, ''):
        
        # this is where data from websocket client comes from line by line
        line = line.strip()
        try:
            #parsed_json = json.loads(line)
            sessions[cookie]['ws'].write_message(line)
        except:
            # can't send to websocket? probably we shoud do something nice... TODO
            pass

    try:
        sessions[cookie]['ws'].close() # close websocket - pipe thread is alsmost terminated at this point
    except:
        pass


# ------------------------------
#        Tornado handlers
# ------------------------------
class IndexHandler(web.RequestHandler):
    @web.asynchronous
    def get(self):
        
        # set new cookie on page open of page refresh
        id = str(uuid.uuid1())
        self.set_secure_cookie("ids", id)
        session={}
        session["cookie"] = self
        sessions[id] = session
        self.render("index.html", server_url=options.host, server_port=options.port) 


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    @web.asynchronous
    def open(self):
        global sessions
        cookie = self.get_secure_cookie("ids")
        session={}
        session = sessions[cookie]
        session["ws"] = self
        sessions[cookie] = session

        cmd = ['python', 'client.py']
        thread.start_new_thread(pipe_thread, (cmd, cookie))


    @web.asynchronous
    def on_message(self, message):
        global sessions
        cookie = self.get_secure_cookie("ids")
        sessions[cookie]['pipe'].stdin.write(message)
        sessions[cookie]['pipe'].stdin.flush()


    @web.asynchronous
    def on_close(self):
        global sessions
        cookie = self.get_secure_cookie("ids")
        sessions[cookie]['pipe'].kill()  # kill process
        del sessions[cookie]             # delete dictionary record


settings = {
    "cookie_secret": str(uuid.uuid1()),
    "xsrf_cookies": True
}

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': './'}),
], **settings)


# ------------------------------
#            MAIN
# ------------------------------
logging.getLogger('tornado.access').disabled = True # disable logging to console

# parse commandline arguments

# example: app.py --port=7777 --host=192.168.100.21 -> when serving clients from other hosts
# example: app.py -> when running on localhost

define("host", default="localhost", help="app host", type=str)
define("port", default=7777, help="WWW port", type=int)
options.parse_command_line()
print("> Listening HTTP on %s:%d" % (options.host, options.port))

#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.bind((options.host, options.tcpport))
#serversocket.listen(4)

signal.signal(signal.SIGINT, signal_handler)
app.listen(options.port)
ioloop.PeriodicCallback(try_exit, 100).start() 
ioloop.IOLoop.instance().start()
