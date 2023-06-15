from flask import Blueprint,render_template,request,jsonify
from pickle import load
import pandas as pd

controller = Blueprint("controller",__name__)

symptoms_dict = {
    "itching": "Itching",
    "skin_rash": "Skin rash",
    "continuous_sneezing": "Continuous sneezing",
    "chills": "Chills",
    "joint_pain": "Joint pain",
    "stomach_pain": "Stomach pain",
    "acidity": "Acidity",
    "muscle_wasting": "Muscle wasting",
    "vomiting": "Vomiting",
    "fatigue": "Fatigue",
    "weight_gain": "Weight gain",
    "anxiety": "Anxiety",
    "mood_swings": "Mood swings",
    "weight_loss": "Weight loss",
    "restlessness": "Restlessness",
    "cough": "Cough",
    "high_fever": "High fever",
    "breathlessness": "Breathlessness",
    "sweating": "Sweating",
    "indigestion": "Indigestion",
    "headache": "Headache",
    "nausea": "Nausea",
    "loss_of_appetite": "Loss of appetite",
    "back_pain": "Back pain",
    "constipation": "Constipation",
    "abdominal_pain": "Abdominal pain",
    "diarrhoea": "Diarrhoea",
    "mild_fever": "Mild fever",
    "swelling_of_stomach": "Swelling of stomach",
    "malaise": "Malaise",
    "phlegm": "Phlegm",
    "throat_irritation": "Throat irritation",
    "redness_of_eyes": "Redness of eyes",
    "sinus_pressure": "Sinus pressure",
    "runny_nose": "Runny nose",
    "congestion": "Congestion",
    "chest_pain": "Chest pain",
    "weakness_in_limbs": "Weakness in limbs",
    "fast_heart_rate": "Fast heart rate",
    "neck_pain": "Neck pain",
    "dizziness": "Dizziness",
    "cramps": "Cramps"
}

symptomps_score = pd.read_csv("csv/Symptom-severity.csv")
symptomps_precaution = pd.read_csv("csv/symptom_precaution.csv")
symptomps_description = pd.read_csv("csv/symptom_Description.csv")

@controller.route("/")
def index():
    return render_template("index.html",index=True)

@controller.route("/result")
def result():
    return render_template("result.html",result=True)

@controller.route("/check",methods=["GET","POST"])
def check():
    check_dict = { symptom: 0 for symptom in symptoms_dict }
    symptoms_arr = []
    score_arr = []

    _symptomps_description = dict(zip(symptomps_description["Disease"],symptomps_description["Description"]))
    _symptomps_score = dict(zip(symptomps_score["Symptom"],symptomps_score["weight"]))
    _symptomps_precaution = {}

    key_column = 'Disease'
    value_columns = ["Precaution_1","Precaution_2","Precaution_3","Precaution_4"]

    for _, row in symptomps_precaution.iterrows():
        key = row[key_column]
        values = [row[col] for col in value_columns]
        _symptomps_precaution.setdefault(key, []).extend(values)


    if request.method ==  "POST":
        input_symptomps = request.get_json()["symptoms"]

        for item in input_symptomps:
            # change the input data to dictonary keys
            for key,value in symptoms_dict.items():
                if value == item:
                    symptoms_arr.append(key)

        for symptoms in symptoms_arr:
            check_dict[symptoms] += 1
            score_arr.append(_symptomps_score[symptoms])
        
        with open("model/ml.pickle","rb") as pickled:
            ml = load(pickled)

        _input = [list(check_dict.values()) + [0 for i in range(0,90)]] 
        _result = ml.predict(_input)[0]
        precaution = [x for x in _symptomps_precaution[_result] if not None ]
        description = _symptomps_description[_result]

        return jsonify(msg="success",name=_result,precaution=precaution,description=description)


    return render_template("cek_penyakit.html",symptoms=list(symptoms_dict.values()),_input=True)

@controller.route("/detail")
def detail():
    return render_template("detail.html",about=True)

@controller.route("/about")
def about():
    return render_template("about.html",about=True)


