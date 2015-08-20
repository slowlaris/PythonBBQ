#!/usr/bin/env python
# encoding: utf-8

import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;

def main():
#-------------------------获取源码---------------------------------------------------------
    # 定义url
    usermainUrl = "http://www.songtaste.com/user/351979/";
    # 请求url
    req = urllib2.Request(usermainUrl);
    # 打开url
    resp =urllib2.urlopen(req);
    # 读取url全部源码
    respHtml = resp.read();
#-----------------------------方法一:BeautifulSoup------------------------------------------
    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);
    #<h1 class="h1user">crifan</h1>
    foundClassH1user = soup.find(attrs={"class":"h1user"});
    print "foundClassH1user= ",foundClassH1user;
    if(foundClassH1user):
                h1userStr = foundClassH1user.string;
                print "h1userStr=",h1userStr;
#-----------------------------方法二:re----------------------------------------------------
    foundH1user = re.search('<h1\s+class="h1user">(?P<whoareyou>\w+)</h1>',respHtml);
    # 打印匹配的文本
    print "foundH1user=",foundH1user.group(0);
    # 获取匹配的文本中的分组的值
    if(foundH1user):
                h1user = foundH1user.group("whoareyou");
                print "h1user=",h1user;
#------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main();
