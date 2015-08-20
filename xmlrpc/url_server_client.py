#!/usr/bin/python
#*- coding: UTF-8 -*-

import xmlrpclib

#proxy = xmlrpclib.ServerProxy("http://www.baidu.com")
proxy = xmlrpclib.ServerProxy("http://www.sogou.com")

try:
    proxy.some_method()
except xmlrpclib.ProtocolError as err:
    print "A protocol error occurred"
    print "URL: %s" % err.url
    print "HTTP/HTTPS headers: %s" % err.headers
    print "Error code: %d" % err.errcode
    print "Error message: %s" % err.errmsg
