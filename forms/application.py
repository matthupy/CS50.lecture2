from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    name = request.form.get("name")
    if name == None or len(name) == 0:
        name = "Stranger"
    return render_template("hello.html", name=name)

if __name__=="__main__":
    app.run()