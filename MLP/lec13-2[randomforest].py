from sklearn import datasets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mnist = datasets.load_digits()
features, labels = mnist.data, mnist.target

def cross_validation(classifier, features, lables):
    cv_scores = []
    for i in range(10):
        scores = cross_val_score(classifier, features, lables, cv=10, scoring='accuracy')
        cv_scores.append(scores.mean())
    return cv_scores

dt_cv_scores = cross_validation(tree.DecisionTreeClassifier(), features, labels)
rf_cv_scores = cross_validation(RandomForestClassifier(), features, labels)

cv_list = [['tree', dt_cv_scores],
           ['forest', rf_cv_scores]]

plt.figure()
plt.plot(cv_list)
plt.show()