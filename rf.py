import glob
import re
import shutil
import os
import pandas
import pickle
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
import seaborn as sns



def main():
    list_of_files = list()
    y = list()
    for filepath in glob.glob('int_tokes/**.func', recursive = True):
        good = False
        name = filepath.rsplit('/')[1]
        if(name.lower().count('good') == 1):
            good = True
        else:
            good = False
        f = open(filepath, "r")
        file_content = f.read()
        file_content = file_content.replace('\n', ' ')
        file_content = file_content.rstrip()
        file_content = file_content.lstrip()
        file_content = file_content.replace('\t', ' ')

        list_of_files.append(file_content)
        if(good == True):
            y.append(1)
        else:
            y.append(0)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_of_files)
    X.toarray()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)
    forest = RandomForestClassifier(n_estimators = 100, verbose=3, n_jobs=-1)
    forest = forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    false_positive, true_positive, _ = roc_curve(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred)
    plt.figure()
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(false_positive, true_positive, color='darkorange', label='Random Forest')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve (area = %0.2f)' % auc)
    plt.legend(loc='best')
    plt.savefig('roc.png')
    plt.show()
    res = confusion_matrix(y_test, y_pred)
    print(res)
    fig = plt.figure(figsize=(10, 7))
    try:
        heatmap = sns.heatmap(res, annot=True,cbar=False)
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=14)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('confusion_matrix.png')
    plt.show()


# Compute micro-average ROC curve and ROC area

if __name__ == '__main__':
    main()
