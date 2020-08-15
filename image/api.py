import flask
from flask import request, jsonify
import json
import pandas
from sklearn.ensemble import RandomForestClassifier  
from sklearn import svm

def read_train_data():
    df = pandas.read_csv('isolet1+2+3+4.data',sep=',', header=None, skiprows=1)
    return df

def read_test_data():
    df=pandas.read_csv('isolet5.data',sep=',',header=None,skiprows=1)
    return df

def get_X(df,features):
    if features==None:
        return df[df.columns[:-1]]
    return df[features]

def get_y(df):
    # class value is the last column in the working dataset
    y= df[df.columns[-1]]
    return y

def classification_rate(features):
    
    train_data=read_train_data()
    test_data=read_test_data()
    
    X_train = get_X(train_data,features)
    y_train= get_y(train_data)

    X_test=get_X(test_data,features)
    y_test=get_y(test_data)
    
    SVM = svm.SVC(decision_function_shape="ovo",gamma="scale").fit(X_train, y_train)  
    return SVM.score(X_test, y_test)

    #RF = RandomForestClassifier(constant.num_estimators_RF).fit(X_train, y_train)   
    #return RF.score(X_test, y_test)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search', methods=['POST'])
def home():

    data=request.form
    print("Hello--"+str(data))
    features=data.get('features')
    features=json.loads(features)
    return str(classification_rate(features))
   
app.run(host='0.0.0.0', port=5000)