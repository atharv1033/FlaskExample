from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Python workshop"
    a = [1,2,3,4,5]
    b = (1,2,3,4,5)
    c = {'a':1,'b':2,'c':3}
    return render_template('tmp.html',name =name,lista = a, tuplea = b,dicta = c,result = c)

if __name__ == '__main__':
    app.run(debug = True)
