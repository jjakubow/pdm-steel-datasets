import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# load the data into Pandas DataFrame
df = pd.read_csv('tcm5_dataset_1.csv')
# make lists with columns related to features and anomalies
anomaly_columns = [c for c in df.columns if 'Anomaly' in c]
feature_columns = [c for c in df.columns if c not in anomaly_columns]
# divide the data into X (features) and Y (labels)
X = df.loc[:, feature_columns]
Y = df.loc[:, anomaly_columns]
# create array which tells us if any type of anomaly is present in the observation
y = (Y.sum(axis=1) != 0).values

# divide dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# define, train and evaluate ML model
iforest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
iforest.fit(X_train)
y_test_pred = iforest.predict(X_test) == -1
f1 = f1_score(y_test, y_test_pred)