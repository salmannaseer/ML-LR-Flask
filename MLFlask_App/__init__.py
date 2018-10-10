from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
@app.route('/')
def hello_world():
    return ML()


def ML():
    # 1. Data Set with different domains
    path_to_file = "insurance_data.csv"
    
    
    # 2. Read the Data frame using pandas in python
    data = pd.read_csv("insurance_data.csv", encoding='utf-8')
    print (type(data))
    
    X = data[['age', 'sex', 'bmi', 'children', 'smoker', 'expenses' ]]
    y = data['insurance']
    
    
    # 3. Split Data it in 80/20 using random (train train split function makes it random unless random_state parameter is used)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    print("Items for training",len(X_train))
    print("Items for test", len(y_test))
    
    # 4. Train the classifier on the 80 sliced data
    model = LogisticRegression()
    model.fit(X_train,y_train)
    
    
    # 5. Evaluate the classifier on the 20 sliced data and share accuracy - max 3 domains are okay
    model.predict(X_test)
    print("Model Accuracy", model.score(X_test, y_test))
    return str(model.score(X_test, y_test))
    
if __name__ == '__main__':
   app.run()