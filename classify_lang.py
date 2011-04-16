import ngram
from xmlIO import *
from math import sqrt
class classify_lang(object):
	def __init__(self,fileName):
		self.sList = readXml(fileName)
		self.n = ngram.ngram()
		self.usedDist = 1;
	def l1_dist(self,hist1,hist2):
		summ = 0
		for i in range(97,123):
			try:
				summ = summ + abs(float(hist1[chr(i)])/float(hist1[str(1)]) - float(hist2[chr(i)])/float(hist2[str(1)]))
			except:
				summ = summ + 0
		return summ
	def l2_dist(self,hist1,hist2):
		summ = 0
		for i in range(97,123):
			try:
				dummy = abs(float(hist1[chr(i)])/float(hist1[str(1)]) - float(hist2[chr(i)])/float(hist2[str(1)]))
				summ = summ +  dummy*dummy
			except:
				summ = summ + 0
		return summ
	def bc_dist(self,hist1,hist2):
		summ = 0
		for i in range(97,123):
			try:
				summ = summ + sqrt(abs(float(hist1[chr(i)])/float(hist1[str(1)]) * float(hist2[chr(i)])/float(hist2[str(1)])))
			except:
				summ = summ + 0
		return summ

	def classify(self,inpStr):
		l1Decision=" "
		l2Decision=" "
		bcDecision=" "
		l1Val=1
		l2Val=1
		bcVal=0

		self.n.clearsList()
		for x in inpStr.lower().split():
			self.n.update(x,"Dummy")
		sListInp = self.n.getsList()
		for x in self.sList:
			if self.l1_dist(self.sList[x],sListInp["Dummy"])<l1Val:
				l1Val = self.l1_dist(self.sList[x],sListInp["Dummy"])
				l1Decision = x
			if self.l2_dist(self.sList[x],sListInp["Dummy"])<l2Val:
				l2Val = self.l2_dist(self.sList[x],sListInp["Dummy"])
				l2Decision = x
			if self.bc_dist(self.sList[x],sListInp["Dummy"])>bcVal:
				bcVal = self.bc_dist(self.sList[x],sListInp["Dummy"])
				bcDecision = x
		print l1Decision,l2Decision,bcDecision
