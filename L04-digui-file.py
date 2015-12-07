#!/usr/bin/env python
#-*- coding=utf-8 -*-
##############################
import os
def scandir(target):
        for obj in os.listdir(os.curdir):
                if os.path.isfile(obj):
                        if target in obj:
                                print obj,
                        else:
                                pass
                if os.path.isdir(obj):
                        os.chdir(obj)
                        scandir('txt')
                        os.chdir(os.pardir)
scandir('txt')
