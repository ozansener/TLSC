# -*- coding: utf-8 -*-
from rss import *

global letterList
sList = {} # içerisine nGram şeyleri doldurulacak. her dilinki ayrı ayrı tabi.

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
            "\\":""} #buraya xD, :S fln gibi smileyler de eklenebilir.

feedList = ["cnn.xml","bbc.xml"] #buraya kontrol edilecek feedlerin listesi eklenmeli.

#harfleri küçültmek için str(hede).lower() mevcuttur.
def repChar(inputStr,charDict):
    ret = inputStr.encode("utf-8")
    for x in charDict:
        ret = ret.replace(x,charDict[x])
    return ret

#harfleri ayırmak için str(hede).split() mevcut. split(",",2) dersem 2 defa , olan yerden ayırır. 

kedi = "the cat sat on the mat! so i shouted at him!!!"

kedi = repChar(kedi,charList)
print kedi.split()

def nGram(inputStr,nMax,lang):
    #string'in (n-1)inci karakterinden başlayarak stringin sonuna kadar for ile tara. sonra bu taradığın şeyleri otomatik olarak letterList'e ekle.
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
                letterList[str(maxGram)] = letterList[str(maxGram)] + 1
            except:
                letterList[str(maxGram)] = 1
            try:
                letterList[inputStr[fPoint:lPoint]] = letterList[inputStr[fPoint:lPoint]] + 1
            except:
                letterList[inputStr[fPoint:lPoint]] = 1
            fPoint = fPoint + 1 #bunu kısayolu ne?
            lPoint = lPoint + 1
        maxGram = maxGram - 1
    sList[lang] = letterList

nVal = 1 #nGram'ın n'si

def fonksiyon(): #isim bulamadım :D
    for x in feedList:
        #burada feedlist'teki url'yi indir.
        feed = getFeed(x)
        #indirdikten sonra üstteki fonksiyonu da değiştir.
        for channel in feed:
            print "Feed: %s, %s" %(channel["title"],channel["desc"])
            print "Language: %s" %(channel["lang"])
            for obj in channel["titles"]:
                for x in repChar(obj["title"],charList).lower().split():
                    nGram(x,nVal,channel["lang"])
                for x in repChar(obj["desc"],charList).lower().split():
                    nGram(x,nVal,channel["lang"])



fonksiyon()
print sList

