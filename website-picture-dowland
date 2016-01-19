#!/usr/bin/env python
#-*- coding=utf-8 -*-
##############################
import time,re
import requests
class zhuaqu(object):
        def __init__(self):
                self.pict_list = list()
        def __str__(self):
                return 'Object %s'%(self.pict_list)
        __repr__ = __str__
        def __read_html(self,domain):
                content = str(requests.get(domain).content)
                full_content = content.split('\n')
                return full_content
        def __format_pict(self):
                return re.compile(r'.*(http.+?\.jpg|http.+?\.png|http.+?\.gif)')
        def __picture_list(self,domain):
                full_content = self.__read_html(domain)
                format_pipei = self.__format_pict()
                for line in full_content:
                        if format_pipei.search(line):
                                xxx = "".join(format_pipei.findall(line))
                                self.pict_list.append(xxx)
                        else:
                                pass
                return self.pict_list
        def main(self,domain):
                for line in self.__picture_list(domain):
                        f = file(line.split('/')[-1],'wb')
                        pict_content = requests.get(line,verify=False).content
                        f.write(pict_content)
                        f.close()
a = zhuaqu()
a.main('http://douban.com/')
