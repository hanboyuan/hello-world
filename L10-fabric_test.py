# -*- coding=utf-8 -*-
###############################
from fabric.api import run


def host_type():
    run('hostname')


print host_type()
