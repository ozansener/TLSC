import ngram
class classify_lang(object):
	def __init__(self,fileName):
		#Load File
		self.n = ngram.ngram():
		self.usedDist = 1;
	def l1_dist(self,vector1,vector2):
	def l2_dist(self,vector1,vector2):
	def bc_dist(self,vector1,vector2):
	def classify(self,inpStr):
		self.n.clearsList()
		self.n.update(inpStr,'Dummy')
		sList = self.n.getsList()
		#Do extra stuff
