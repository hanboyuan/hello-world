#!/usr/bin/env python
# -*- coding=utf-8 -*-
######################
import os


def find_filenum(path):
    aa = list()
    for root, dirs, files in os.walk(path):
        aa = aa + files
    num = len(aa)
    aa = list()
    return num

if __name__ == "__main__":
    print find_filenum('./')
