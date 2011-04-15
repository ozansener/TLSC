# -*- coding: utf-8 -*-
from rss import *

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

def nGram(inputStr,nMax,lang):
    #It calculates all n-grams such that 1<=n<=nMax
    try:
        letterList = sList[lang]
    except:
        letterList = {}
    maxGram = len(inputStr)
    if maxGram > nMax:
        maxGram = nMax
    while maxGram > 0:
        fPoint = 0
        lPoint = maxGram
        while lPoint < len(inputStr) + 1:
            try:
                letterList[str(maxGram)] = letterList[str(maxGram)] + 1 #Total number of each n letter sets
            except:
                letterList[str(maxGram)] = 1
            try:
                letterList[inputStr[fPoint:lPoint]] = letterList[inputStr[fPoint:lPoint]] + 1 #Value of a number of a letter
            except:
                letterList[inputStr[fPoint:lPoint]] = 1
            fPoint = fPoint + 1 
            lPoint = lPoint + 1
        maxGram = maxGram - 1
    sList[lang] = letterList

nVal = 1 #We only consider 1 gram (currently :p)

def processFeeds():
    for x in feedList:
        feed = getFeed(x)
        for channel in feed:
            print "Feed: %s, %s" %(channel["title"],channel["desc"])
            print "Language: %s" %(channel["lang"])
            for obj in channel["titles"]:
                for x in repChar(obj["title"],charList).lower().split():
                    nGram(x,nVal,channel["lang"])
                for x in repChar(obj["desc"],charList).lower().split():
                    nGram(x,nVal,channel["lang"])



processFeeds()
print sList

