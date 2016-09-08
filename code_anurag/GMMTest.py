import os
import numpy as np
from sklearn import mixture
import pickle

def loadGMM(gmmFile):
	gmm = pickle.load(open(gmmFile,'rb'))
	gmm.covars_ = np.load(gmmFile+'_01.npy')
	gmm.weights_ = np.load(gmmFile+'_02.npy')
	gmm.means_ = np.load(gmmFile+'_03.npy')
	return gmm

def testFiles(filelist, gmmFileDir, ncomps, outfile):
	gmm_P = loadGMM(gmmFileDir+"P/"+str(ncomps)+"/sklearnGMM.pkl")
	gmm_N = loadGMM(gmmFileDir+"N/"+str(ncomps)+"/sklearnGMM.pkl")
	# gmmext_P = gmmFileDir+"P/"+str(ncomps)+"/sklearnGMM.pkl"
	# gmmext_N = gmmFileDir+"N/"+str(ncomps)+"/sklearnGMM.pkl"
	# print 'loading gmm'
	# gmm_P = pickle.load(open(gmmFile,'rb'))
	# x = np.load(gmmext_P+'_01.npy')
	# gmm_P.covars_=x
	# # print x
	# x = np.load(gmmext_P+'_02.npy')
	# gmm_P.weights_=x
	# # print x
	# x = np.load(gmmext_P+'_03.npy')
	# gmm_P.means_=x
	# print x
	# return
	print 'reading filelist'
	flist = open(filelist, 'r')
	files = flist.readlines()

	'compiling data'
	alldata = None
	files = map(lambda x: '../'+x, files)
	np.random.shuffle(files)
	out = open(outfile, 'w')
	for fl in files:
		print "reading ", fl
		data = np.loadtxt(fl.strip(),delimiter=',')
		# data = data.reshape(1, -1)
		# alldata = alldata.getA1()
		ll_P = sum(gmm_P.score(data))
		ll_N = sum(gmm_N.score(data))
		
		label = "N"
		if ll_P > ll_N:
			label = 'P'
		out.write(str(ll_P)+ str(ll_N) + '\n')
	out.close()

testFiles('../files/folds/BR/BR_p.fold0', '../GMMs/BR/fold_0/', 1, "test_result.txt")