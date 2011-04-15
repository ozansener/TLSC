# -*- coding: utf-8 -*-
from rss import *
from pylab import *
import ngram

global letterList
sList = {} # içerisine nGram şeyleri doldurulacak. her dilinki ayrı ayrı tabi.

# Conversion of some turkish language specific characters
charList = {"\x80":"c",
            "\x8e":"a",
            "\x99":"o",
            "\xa3":"u",
            chr(0xe2):"o", # 0xe2 karakterini silemiyorum!!! :S
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

feedList = ["cnn.xml","bbc.xml"] #If new feeds want to be precessed, can be added to here

#Replace language specfiic characters
def repChar(inputStr,charDict):
    ret = inputStr.encode("utf-8")
    for x in charDict:
        ret = ret.replace(x,charDict[x])
    return ret

kedi = "the cat sat on the mat! so i shouted at him!!!"

kedi = repChar(kedi,charList)
print kedi.split()

n=ngram.ngram()
def processFeeds():
    for x in feedList:
        feed = getFeed(x)
        for channel in feed:
            print "Feed: %s, %s" %(channel["title"],channel["desc"])
            print "Language: %s" %(channel["lang"])
            for obj in channel["titles"]:
                for x in repChar(obj["title"],charList).lower().split():
                    n.update(x,channel["lang"])
                for x in repChar(obj["desc"],charList).lower().split():
                    n.update(x,channel["lang"])



def plotHistograms(values):
	print values
	array=[];
	for i in range(97,123):
		try:
			array.append(values[chr(i)]/float(values["1"]))
		except:
			array.append(0)
	xAxis = range(97,123)
	plot(xAxis,array) 	
	print array
	
processFeeds()
x=1
a=n.getsList();
for i in a:
	subplot(2,1,x)
	plotHistograms(a[i])
	x=x+1
show()
