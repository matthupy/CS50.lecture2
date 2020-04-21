from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/{name}")
def david():
    return "Hello, {name}!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"

if __name__ == "__main__":
    app.run()