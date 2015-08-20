#!/usr/bin/python
#-*- coding: UTF-8 -*-

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")

print "3 is even: %s" % str(proxy.is_even(3))#客户端调用XML-RPC函数
print "100 is even: %s" % str(proxy.is_even(100))
