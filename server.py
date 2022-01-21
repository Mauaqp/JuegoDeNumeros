from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = "estoessecreto"

#Ruta index
@app.route('/')
def index():
    ran = random.randint(1,100)
    print("El numero aleatorio es " + str(ran))
    session["ran"] = ran
    return render_template("index.html")

#Ruta guess
@app.route('/guess',methods=['POST'])
def guessNum():
    guess = {
        "numero" : request.form["numero"]
    }
    session["numero"] = int(request.form["numero"])

    if guess["numero"] == session["ran"]:
        print("Adivinaste")
        
    else:
        print("No adivinaste")
    return redirect('/')

#app.run
if __name__=="__main__":   
    app.run(debug=True)    