from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    user = {'username':'Dhiraj'}
    posts = [
            {
                'author': {'username': 'Daniel'},
                'body' : 'Beautiful day in Shrilanka!'
                },
            {
                'author' : {'username': 'Amar'},
                'body' : 'Tiger Zinda hai hai movie was so cool!'
                }
        ]
    
    return render_template('exerciseTmp.html',user=user, posts=posts)

if __name__ == '__main__':
    app.run(debug = True)
