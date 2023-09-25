from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    html = """
<form action="http://127.0.0.1:8080/api/">
 <label>a:</label><br>
 <input type="text"  name="a" value="0"><br>
 <label>b:</label><br>
 <input type="text" name="b" value="0"><br><br>
 <input type="submit" value="Submit">
</form>
"""
    return html

@app.route("/about/")
def about():
    return "<h1>About Page</h1>"

@app.route("/api/<float:n>")
def home(n):
    print(type(n))
    return {"n": n}

if __name__ == "__main__":
    app.run(port='8080', debug=True)