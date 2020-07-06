import constant
import pandas 

def read_train_data():
    df = pandas.read_csv(constant.train_data_path,sep=',', header=None, skiprows=1)
    return df

def read_test_data():
    df=pandas.read_csv(constant.test_data_path,sep=',',header=None,skiprows=1)
    return df