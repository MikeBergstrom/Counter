from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'ThisIsSecret'

@app.route('/')

def index():
  session['count'] = session['count'] +1  
  return render_template("index.html")

@app.route('/button', methods=['POST'])
def button():
    if request.form['action'] == 'twotimes':
        session['count'] = session['count'] +1
        return redirect('/')
    elif request.form['action'] == 'reset':
        session['count'] = 0
        return redirect('/')
    
app.run(debug=True)