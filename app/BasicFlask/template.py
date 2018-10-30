from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name='Python Flask Workshop'
    return render_template('tmp.html',name1=name)

@app.route('/list')
def list():
    mylist=[12,23,34,45,56]
    return render_template('tmp.html',list=mylist)

@app.route('/dict')
def dict():
    mydict={1:'akash',2:'hemanshu'}
    return render_template('dict.html',dict=mydict)

##@app.route('/tuple')


if __name__ == '__main__':
    app.run(debug=True)
