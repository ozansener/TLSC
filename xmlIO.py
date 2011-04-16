from xml.etree import ElementTree as ET

def writeXml(inputDict, xmlLoc): #inputDict = sList, xmlLoc = location of xml
    rootElement = ET.Element("TLSC")
    for language in inputDict:
        langElement = ET.SubElement(rootElement,"LANGUAGE")
        langElement.set("lang",str(language))
        for obj in inputDict[language]:
            objElement = ET.SubElement(langElement,"OBJECT")
            objElement.set("count",str(inputDict[language][obj]))
            objElement.text = obj.replace(chr(0xe2),"").replace(chr(0xe3),"").replace(chr(0xe4),"e")
    xmlTree = ET.ElementTree(rootElement)
    xmlTree.write(xmlLoc)
        
