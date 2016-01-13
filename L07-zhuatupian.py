#!/usr/bin/env python
#-*- coding=utf-8 -*-
##########################
import requests
from db import db_picture
class zhuatupian(object):
	def __init__(self,picture):
		self.picture = picture
	def __str__(self):
		return "Object zhuatupian : %s"%(self.picture)
	def download(self):
		for name,url in self.picture.items():
			temp = requests.get(url)
			f = file("%s"%(name),'wb')
			f.write(temp.content)
			f.close()

a1 = zhuatupian(db_picture)
a1.download()
