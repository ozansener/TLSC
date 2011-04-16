import ngram
import process_rss
from pylab import *


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
	
x=1

r=process_rss.process_rss()
r.add_rss("cnn.xml")
r.add_rss("bbc.xml")
r.process()
n=r.getNgram()
a=n.getsList();
for i in a:
	subplot(2,1,x)
	plotHistograms(a[i])
	x=x+1
show()
