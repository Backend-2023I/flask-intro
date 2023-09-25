from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello world"

@app.route("/home")
def home():
    return "Home Page"

if __name__ == "__main__":
    app.run(port='8080', debug=True)