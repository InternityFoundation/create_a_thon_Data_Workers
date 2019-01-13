#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
df=pd.read_csv("data.csv")
df.keys()
df.shape
df.head()

X=df.iloc[:,2:-1]
y=df.iloc[:,1]


'''#categorial of data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)'''

#visualizing the data
sns.pairplot(df,hue="diagnosis",vars=["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean"])
sns.countplot(df.diagnosis)
#sns.scatterplot(x="radius_mean",y="smoothness_mean",hue="diagnosis",data=df)

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


#feature scaling 
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
'''classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)'''
param_grid={'C':[0.1,1,10,100],"gamma":[1,0.1,0.01,0.001],"kernel":["rbf"]}
from sklearn.model_selection import GridSearchCV
grid=GridSearchCV(SVC(),param_grid,refit=True,verbose=4)
grid.fit(X_train,y_train)

grid.best_params_

# Predicting the Test set results
grid_pred=grid.predict(X_test)

#evaluating the model by confusion matrix
from sklearn.metrics import confusion_matrix,classification_report
cm = confusion_matrix(y_test, grid_pred)
sns.heatmap(cm,annot=True,xticklabels=["b","m"], yticklabels=["b","m"])


# to check accuracy
print(classification_report(y_test,grid_pred))

# predict a new single observation
# new_pred=grid.predict(sc.transform(np.array([[13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]])))
# To convert series into dataFrame
import socket as sk
s=sk.socket()
host = sk.gethostname() 
port = 50000                
s.bind((host, port))        
                 
while True:
   s.listen()
   c, addr = s.accept()
   msg=c.recv()
   arr=msg.split(',')
   new_pred=grid.predict(sc.transform(np.array([[float(arr[0]),float(arr[1]),float(arr[2]),float(arr[3]),float(arr[4]),float(arr[5]),float(arr[6]),float(arr[7]),float(arr[8]),float(arr[9]),float(arr[10]),float(arr[11]),float(arr[12]),float(arr[13]),float(arr[14]),float(arr[15]),float(arr[16]),float(arr[17]),float(arr[18]),float(arr[19]),float(arr[20]),float(arr[21]),float(arr[22]),float(arr[23]),float(arr[24]),float(arr[25]),float(arr[26]),float(arr[27]),float(arr[28]),float(arr[29])]])))
   new_pred = pd.DataFrame(new_pred)
   new_pred = new_pred.convert_objects(convert_numeric=True)
   mr=new_pred['0'].values[0]
   if mr=="B":
       sm="BENIGN"
   else:
       sm="MALIGNANT"
   c.send(sm)
    
