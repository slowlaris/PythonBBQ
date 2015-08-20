#!/usr/bin/env python
# encoding: utf-8

import urllib

def GetStatusCode(url):
    statuscode = urllib.urlopen(url).getcode()
    return statuscode==200

if __name__ == "__main__":
    result = 0;
    url = raw_input("请输入需要测试的网址: ");
    num = input("请输入需要循环的次数: ");
    for i in range(0,num):
        if (GetStatusCode(url) == True):
            result +=1;
    print('Test ' + str(num) +' times, succeed '+str(result) +' times')
