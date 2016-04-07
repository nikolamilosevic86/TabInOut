'''
Created on 10 Mar 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from sklearn import svm
if __name__=="__main__":
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y) 
    
    print clf.predict([[2., 2.]])