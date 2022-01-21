from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = "estoessecreto"

#Ruta index
@app.route('/')
def index():
    if "ran" not in session:
        session["ran"] = random.randint(1,100)
    print("El numero aleatorio es " + str(session["ran"]))
    return render_template("index.html")

#Ruta guess
@app.route('/guess',methods=['POST'])
def guess():
    session['numero'] = int(request.form['numero'])
    return redirect('/')

#Ruta reset
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

#app.run
if __name__=="__main__":
    app.run(debug=True)