class ngram(object):
	def __init__(self):
		self.n = 1
		self.sList={};
		
	def update(self,inputStr,lang):
		try:
			letterList = self.sList[lang]
		except:
			letterList = {}
		maxGram = len(inputStr)
		if maxGram > self.n:
        		maxGram = self.n
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
		self.sList[lang] = letterList
	def getsList(self):
		return self.sList
	def clearsList(self):
		self.sList = {}
