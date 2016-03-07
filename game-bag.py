#/usr/bin/env python
# -*- coding=utf-8 -*-
##############################
class bag(object):
    def __init__(self):
        self.result = list()
        self.len = len(self.result)

    def add(self, item):
        self.result.append(item)

    def remove(self, item):
        self.result.remove(item)

    def __len__(self):
        return len(self.result)

    def __iter__(self):
        return self

    def next(self):
        if self.len == 0:
            raise StopIteration()
        self.len = self.len - 1
        return self.result[self.len]
