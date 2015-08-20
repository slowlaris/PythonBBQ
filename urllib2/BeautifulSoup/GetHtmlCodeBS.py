#!/usr/bin/env python
# encoding: utf-8

import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;

def main():
    # 定义url
    usermainUrl = "http://www.songtaste.com/user/351979/";
    # 请求url
    req = urllib2.Request(usermainUrl);
    # 打开url
    resp =urllib2.urlopen(req);
    # 读取url全部源码
    respHtml = resp.read();

    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);
    #<h1 class="h1user">crifan</h1>
    foundClassH1user = soup.find(attrs={"class":"h1user"});
    print "foundClassH1user= ",foundClassH1user;
    if(foundClassH1user):
                h1userStr = foundClassH1user.string;
                print "h1userStr=",h1userStr;

if __name__ == "__main__":
    main();
