from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
# import pickle

# frame = pd.read_csv("csv/symptom_Description.csv")
# _frame = pd.read_csv("csv/Symptom-severity.csv")

# training_frame = pd.DataFrame({"disease": frame["Disease"]})
# for row in _frame["Symptom"]:
#     training_frame[row] = 0

# _frame = pd.read_csv("csv/Symptom-severity.csv")


# frame = pd.read_csv("csv/dataset.csv")
# frame_new = (frame.drop('Disease', axis = 1).fillna(''))

# def arr(data):    
#     return ' '.join(data.values)

# simptoms_list = frame_new.apply(arr, axis=1).values.tolist()
# vectorizer = CountVectorizer()

# vector = vectorizer.fit_transform(simptoms_list)

# my_frame = pd.DataFrame(vector.toarray(), columns= vectorizer.get_feature_names_out())

# symptoms_list = vectorizer.get_feature_names_out()
 
# my_frame.insert(0,"Disease",frame["Disease"].map(str.strip))

# my_frame.to_csv("csv/frame.csv")
# 
# scores = pd.read_csv("csv/Symptom-severity.csv")
# scores = dict(zip(scores.Symptom,scores.weight))
# 

# # def labeling(data):
# #     data = data.str.strip() if data.dtype == "object" else data
# #     for x in range(1,18):
# #         data[f"Symptom_{x}"] = scores[data[f"Symptom_{x}"]]
# #     return data

# # frame  = pd.read_csv("csv/dataset.csv",skipinitialspace=True).apply(labeling,axis=1)
# # frame.fillna(0).to_csv("csv/frame.csv")

frame = pd.read_csv("csv/frame.csv")

x = frame.drop(["Disease","Unnamed: 0"],axis=1)
y = frame["Disease"]


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.35,random_state=5)

classifier = SVC()
classifier.fit(x_train,y_train)
training = classifier.predict(x_test)
print(training)
print("Accuracy: ", accuracy_score(training,y_test))

# pickle.dump(classifier,open("model/ml.pickle","wb"))
