from sklearn.ensemble import RandomForestClassifier  
import constant
import reader

def classification_rate(features):

    train_data=reader.read_train_data()
    test_data=reader.read_test_data()

    X_train = get_X(train_data,features)
    y_train= get_y(train_data)

    X_test=get_X(test_data,features)
    y_test=get_y(test_data)

    RF = RandomForestClassifier(constant.num_estimators_RF).fit(X_train, y_train)   
    return RF.score(X_test, y_test)

def get_X(df,features):
    if features==None:
        return df[df.columns[:-1]]
    return df[features]

def get_y(df):
    # class value is the last column in the working dataset
    y= df[df.columns[-1]]
    return y