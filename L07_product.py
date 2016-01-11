#!/usr/bin/env python
#-*- coding=utf-8 -*-
##############################
import datetime
class product(object):
        def __init__(self,name,price):
                self.name = name
                self.price = int(price)
                self.account = self.price
                self.current_week = int(datetime.date.today().isoweekday())
        def __str__(self):
                return "product object (name:%s price:%s)"%(self.name,self.price)
        __repr__ = __str__

        def manjian_100_20(self):
                if self.account >= 100:
                        self.account = self.account - 20
                        #return self.account

        def bazhe(self):
                #print self.current_week
                if self.current_week == 6 or self.current_week == 7:
                        self.account = self.account * 0.8
                        #return self.account
                else:
                        pass
        def account_jiesuan(self):
                        self.manjian_100_20()
                        self.bazhe()
                        return self.account
a = product('computer',2000)
print a.account_jiesuan()
