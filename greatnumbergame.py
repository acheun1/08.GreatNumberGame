#Great Number Game
#2018 10 03
#Cheung Anthony

# When you build this, please make sure that your program meets the following criteria:

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

import random
magicnumber=random.randrange(0,101)
#magicnumber=10

#our index route will handle the form
@app.route('/')
def index():
    return render_template('index.html')

#route to handle form submission that calls HTTP allowed for this route
@app.route('/', methods=['POST'])
def results():
    guesstaken_str=str(request.form['guesstaken'])
    if not guesstaken_str.strip():
        session['guess']='0'
        session.clear()
    elif guesstaken_str.strip():         
        guess_taken_int=int(request.form['guesstaken'])
        if guess_taken_int>magicnumber:
            session['guess']='1'
        if guess_taken_int<magicnumber:
            session['guess']='2'
        if guess_taken_int==magicnumber:
            session['guess']='3'
            session['bingo']=str(magicnumber)
    return redirect('/')
#put return in the statement?        

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
