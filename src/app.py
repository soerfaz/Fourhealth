from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",index=True)

@app.route("/result")
def result():
    return render_template("result.html",result=True)

@app.route("/cek_penyakit",methods=["GET","POST"])
def cek_penyakit():
    return render_template("cek_penyakit.html",_input=True)

@app.route("/detail")
def detail():
    return render_template("detail.html",about=True)

@app.route("/about")
def about():
    return render_template("about.html",about=True)


app.run(debug=True,port=8000)