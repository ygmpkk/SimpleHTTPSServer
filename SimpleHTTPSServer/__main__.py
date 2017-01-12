#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import BaseHTTPServer
import SimpleHTTPServer
import socket
import ssl


def main():
    ssl_file = '/tmp/simple-https-ssl.pem'
    os.system('openssl req -new -x509 -keyout {F} -out {F} -days 365 -nodes -subj "/C=CN/ST=Hangzhou/L=China/CN=www.huijieapp.com"'.format(F=ssl_file))

    httpd = BaseHTTPServer.HTTPServer(

        ('0.0.0.0', 4443),
        SimpleHTTPServer.SimpleHTTPRequestHandler
    )

    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile=ssl_file
    )

    print "Start HTTPS"
    print "https://127.0.0.1:4443"

    httpd.serve_forever()

if __name__ == '__main__':
    main()
