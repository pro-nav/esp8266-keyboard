from http.server import BaseHTTPRequestHandler, HTTPServer
from ctypes import *
from time import sleep

user32 = windll.user32
kernel32 = windll.kernel32
delay = 0.01

keys = {
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87
}


def press(key):
    user32.keybd_event(key, 0, 0, 0)
    sleep(delay)
    user32.keybd_event(key, 0, 2, 0)
    sleep(delay)


class RequestHandler_httpd(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)
        null, msg, mid = self.requestline.split(" ")[1].split("/")
        if(mid):
            press(keys[msg])
        self.send_response(200)

        return


server_address_httpd = ('192.168.43.130', 8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('start')
httpd.serve_forever()
