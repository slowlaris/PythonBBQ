#!/usr/bin/python
#*- coding: UTF-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer

def add():
    return x+y+0j

server = SimpleXMLRPCServer(("localhost",8000))

print "Listening on port 8000..."

server.register_function(add,'add')

server.serve_forever()
