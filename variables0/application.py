from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

if __name__ == "__main__":
    app.jinja_env.auto_reload=True
    app.run(debug=True)