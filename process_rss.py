# -*- coding: utf-8 -*-
from rss import *
from xmlIO import *
import ngram

class process_rss(object):
	def __init__(self):
		# Conversion of some turkish language specific characters
		self.charList = {"\x80":"c",
			"\x8e":"a",
			"\x99":"o",
			"\xa3":"u",
			"\x81":"",
			"\x89":"",
			"\x93":"",
			"\x94":"",
			"\xa1":"i",
			"\xad":"",
			"\xb0":"",
			"\xb1":"",
			"\xb3":"",
			"\xba":"",
			"\xe3":"",
			"\xe4":"a",
			chr(0xe2):"o", # 0xe2 karakterini silemiyorum!!! :S
			"é":"e",
			"ğ":"g",
			"ü":"u",
			"ş":"s",
			"ı":"i",
			"ö":"o",
			"ç":"c",
			"Ğ":"G",
			"Ü":"U",
			"Ş":"S",
			"İ":"I",
			"Ö":"O",
			"Ç":"C",
			"!":"",
			",":"",
			".":"",
			";":"",
			":":"",
			")":"",
			"(":"",
			"'":"",
			'"':"",
			"1":"",
			"2":"",
			"3":"",
			"4":"",
			"5":"",
			"6":"",
			"7":"",
			"8":"",
			"9":"",
			"0":"",
			"-":"",
			"_":"",
			"?":"",
			"%":"",
			"$":"",
			"&":"",
			"/":"",
		    "\\":""} #This set is not complete!!
		self.n = ngram.ngram()
		self.feedList = []
	def add_rss(self,fileName):
		self.feedList.append(fileName)
	#Replace language specfiic characters
	def repChar(self,inputStr):
	    ret = inputStr.encode("utf-8")
	    for x in self.charList:
		ret = ret.replace(x,self.charList[x])
	    return ret
	
	def process(self):
		print self.feedList
		for fd in self.feedList:
			feed = getFeed(fd)		
			for channel in feed:
				print "Feed: %s, %s" %(channel["title"],channel["desc"])
				print "Language: %s" %(channel["lang"])
				for obj in channel["titles"]:
					for x in self.repChar(obj["title"]).lower().split():
						self.n.update(x,channel["lang"])
					for x in self.repChar(obj["desc"]).lower().split():
						self.n.update(x,channel["lang"])                
	def getNgram(self):
		return self.n
	def write2file(self,fileName):
		writeXml(self.n.getsList(),fileName)
