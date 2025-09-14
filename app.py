from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Bienvenue Walid – Flask v2 🎉</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

