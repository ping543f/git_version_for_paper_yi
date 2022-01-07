import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
import sklearn
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
import os

def load_file(filename):
    df = pd.read_csv(filename,sep=",")
    df.head()
    names= list(df.columns)
    return names

## Tryout creating and training new models with dataset
def train_new_models(filename,names):
    dataframe = read_csv(filename, names=names)
    dataframe = dataframe.drop([0])
    array = dataframe.values
    X= array[:,0:16]
    y= array[:,17]
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.25)
    automl = AutoML(algorithms=["Random Forest", "Neural Network"],results_path="yis_classifier")
    automl.fit(X_train, y_train)
    predictions = automl.predict(X_test)
    automl.report()


##Load Previously trained model, from which the results are presented in the paper
def load_pretrained_models(filename,names):
    dataframe = read_csv(filename, names=names)
    dataframe = dataframe.drop([0])
    array = dataframe.values
    X= array[:,0:16]
    y= array[:,17]
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.25)
    automl = AutoML(results_path="yis_model")
    predictions = automl.predict(X_test)


if __name__ == '__main__':
    filename= "dataset/is-500.csv"
    names = load_file(filename)
    ##Uncomment the following line to train models as new model
    # train_new_models(filename,names) 
    ##If encounter no such file or directory, please check the directory structure. Code was initially trained on a mac os, linux os also checked. Windows might give some error.
    load_pretrained_models(filename,names)