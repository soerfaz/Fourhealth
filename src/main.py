from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report
import pandas as pd
import pickle


# scores = pd.read_csv("csv/Symptom-severity.csv")
# scores = dict(zip(scores.Symptom,scores.weight))


# def labeling(data):
#     data = data.str.strip() if data.dtype == "object" else data
#     for x in range(1,18):
#         data[f"Symptom_{x}"] = scores[data[f"Symptom_{x}"]]
#     return data

# frame  = pd.read_csv("csv/dataset.csv",skipinitialspace=True).apply(labeling,axis=1)
# frame.fillna(0).to_csv("csv/frame.csv")

frame = pd.read_csv("csv/frame.csv")

x = frame.drop(["Disease","Unnamed: 0"],axis=1)
y = frame["Disease"]


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.35,random_state=5)

classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train,y_train)
# training = classifier.predict(x_test)

# print("Accuracy: ", accuracy_score(y_test,training))
# print(classification_report(y_test,training))

pickle.dump(classifier,open("model/ml.pickle","wb"))