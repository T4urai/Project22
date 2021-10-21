import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle


def scout():
    df=pd.read_excel("Projectdata.xlsx")
    x1=df.drop(['Players','Clubs','Sub','Pen M','Sub','OG','PlayerCategory'],axis=1)
    nan_value=float("NaN")
    x1.replace('-',0,inplace=True)
    y1=df['PlayerCategory']
    features=x1.columns[0:10]

    labelencoder_x1 = LabelEncoder()
    x1['Position'] = labelencoder_x1.fit_transform(x1['Position'])
    y1=labelencoder_x1.fit_transform(y1)
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size=.2, random_state=41)

    from sklearn.preprocessing import MinMaxScaler
    scaler=MinMaxScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)

    clf=RandomForestClassifier(n_jobs=2,random_state=0)
    clf.fit(x_train,y_train)
    pickle.dump(clf,open('player_scout.pkl','wb'))
    model=pickle.load(open('player_scout.pkl','rb'))
    print(model.predict)
   

scout()

      
    