from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",index=True)

@app.route("/result")
def result():
    return render_template("result.html",result=True)

@app.route("/input",methods=["GET","POST"])
def _input():
    return render_template("input.html",_input=True)


app.run(debug=True,port=8000)