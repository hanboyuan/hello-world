#/usr/bin/env python
# -*- coding=utf-8 -*-
########################################
class Subject:
    def __init__(self):
        self.__observer = list()

    def attach(self, observer):
        if observer not in self.__observer:
            self.__observer.append(observer)

    def detach(self, observer):
        try:
            self.__observer.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self.__observer:
            observer.update(self)


class Data(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self.data = 0

    def setData(self, data):
        self.data = data
        self.notify()

    def getData(self):
        return self.data


class HexViewer(object):
    def update(self, subject):
        print "HexViewer, Subject %s has data %d" % (subject.name, subject.getData())


def main():
    data1 = Data('data1')
    data2 = Data('data2')
    view1 = HexViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)
    data1.setData(1)
    data2.setData(2)


if __name__ == "__main__":
    main()
