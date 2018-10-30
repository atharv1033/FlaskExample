from flask import Flask
app = Flask(__name__)

@app.route("/hi/<int:name>")
def hello_int(name):
    return 'Hello int %d !' %name

@app.route("/hi/<float:name>")
def hello_float(name):
    return 'Hello float %f' %name

@app.route("/hi/<name>")
def hello_string(name):
    return 'Hello string %s' %name

if __name__ == '__main__':
    app.run(debug = True)
