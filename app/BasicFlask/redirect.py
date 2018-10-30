from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Administrator area, no guest allowed'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Guest user %s does not have admin rights' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
    app.run(debug=True)
