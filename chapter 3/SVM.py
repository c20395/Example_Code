#Example 3.1 Python SVM Classifications
from sklearn import svm
X = [[170, 70, 10], [180, 80,12], [170, 65, 8],[160, 55, 7]]
y = [0, 0, 1, 1]
clf = svm.SVC()
clf.fit(X, y)
#Predict 
p = clf.predict([[160, 60, 7]])
print(p)
