from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key='labrinth'
import random

# Set our keys if they don't already exist.
@app.route('/')
def index():
    if 'randNum' not in session:
        session['randNum'] = random.randint(1,100)
        session['playerNum']=0
        session['result']=""
    return render_template('number_game.html')

# Compares the user's number to the RNG one and returns session['result'] which can turn on / off 3 classes for low/high/perfect
@app.route('/compare', methods=['POST'])
def compare():
    session['playerNum'] = request.form['playerNum']
    if int(session['playerNum']) == session['randNum']:
        session['result'] = 'perfect'
        return redirect('/')
    if int(session['playerNum']) < session['randNum']:
        session['result'] = 'tooLow'
        return redirect('/')
    if int(session['playerNum']) > session['randNum']:
        session['result'] = 'tooHigh'
        return redirect('/')

# Easy way to reset our session data
@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)