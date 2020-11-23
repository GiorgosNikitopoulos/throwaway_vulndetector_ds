import glob
import re
import shutil
import os
import pandas
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def main():
    list_of_files = list()
    y = list()
    with open('list_of_files.pkl', 'rb') as f:
        list_of_files = pickle.load(f)
    with open('y.pkl', 'rb') as f2:
        y = pickle.load(f2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)
    print(X_train)
    #vectorizer = CountVectorizer()
    #X = vectorizer.fit_transform(list_of_files)
    #X.to_array()
    #y =


if __name__ == '__main__':
    main()
