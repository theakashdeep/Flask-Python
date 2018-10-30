from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    user={'username': 'Akash'}
    posts=[
        {
            'author':{'username':'Akash'},
            'body':'Beautiful day in Srilanka'
        },
        {
            'author':{'username':'Aman'},
            'body':'It is an amazing movie'
        }
        ]                                           
    return render_template('index.html',user=user,posts=posts)
   
if __name__ == '__main__':
    app.run(debug=True)
