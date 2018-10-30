from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/hi/<name>")
def hello_name(name):
    return "Hello %s" %name

@app.route("/hi/<int:age>")
def hello_age(age):
    return "Age= %d" %age

@app.route("/hi/<float:decimal>")
def hello_decimal(decimal):
    return "Decimal= %f" %decimal

if __name__ == "__main__":
    app.run(debug=True)
