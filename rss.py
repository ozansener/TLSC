# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET

def getFeed(feedFile):
# Çıktı biçimi: [{title:"başlık(channel)" vs. titles:[{title1 vs},{title2 vs.}]},{diğer channel}]
#               ||                                   |            |          |||                |
#               ||                                   |            |__dict.___|||                |
#               ||                                   |                        ||                |
#               ||                                   |_alt başlıklar (liste)__||                |
#               ||                                                             |                |
#               ||________________channel'a ait olan dictionary________________|                |
#               |                                                                               |
#               |_____________________________Burası ana liste__________________________________|
#
#İmkanlar: Channel'lar ve başlıklar arasında for kullanılabilir.
#Bilgiler dictionary vasıtasıyla alınabilir.
    xml = open(feedFile,"r").read()
    feed = ET.XML(xml)
    retList = []
    if feed.tag =="rss" and feed.attrib["version"] == "2.0":
        for channel in feed:
            chann = {"title":None,"categ":None,"desc":None,"link":None,"lang":None}
            if channel.tag == "channel":
                titles = []
                for item in channel:
                    if item.tag == "item":
                        obj = {}
                        for element in item: # burası obj{element.tag} = element.text şeklinde de yazılabilir. Ama ben bazı isimleri değiştirmek istedim.
                            if element.tag == "title":
                                obj["title"] = element.text
                            elif element.tag == "category":
                                obj["categ"] = element.text
                            elif element.tag == "description":
                                obj["desc"] = element.text
                            elif element.tag == "link":
                                obj["link"] = element.text
                            elif element.tag == "guid":
                                obj["guid"] = element.text
                            elif element.tag == "pubDate":
                                obj["date"] = element.text
                        titles.append(obj)
                    elif item.tag == "title":
                        chann["title"] = item.text
                    elif item.tag == "link":
                        chann["link"] = item.text
                    elif item.tag == "description":
                        chann["desc"] = item.text
                    elif item.tag == "language":
                        chann["lang"] = item.text
                chann["titles"] = titles
            retList.append(chann)
    else:
        print "Not implemented yet!"
        #TODO: Add support for ATOM and RSS1
    return retList

