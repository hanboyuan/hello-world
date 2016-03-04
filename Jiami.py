# -*- coding=utf-8 -*-
################################
import hashlib


def jiami(src):
    '''
        通过hash不可逆来进行数据加密，判断加密后数据是否一致来验证
    '''
    return hashlib.sha1(src).hexdigest()
