from flask import Flask ,render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy 
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dgsdgj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
def hash1(nome,cognome):
    s = nome+cognome
    si = len(s)
    a = 0
    for i in range(si):
        a+=ord(s[i])
    return a

class Scomessa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ore = db.Column(db.Integer, nullable = False)
    minuti = db.Column(db.Integer, nullable = False)
    nome = db.Column(db.String(80), nullable = False)
    cognome = db.Column(db.String(80), nullable = False)
    password = db.Column(db.Integer, nullable = False)
@app.route('/', methods=['GET','POST'])
def sito():
    if request.method == 'POST':
        ore = request.form['ore']
        minuti = request.form['minuti']
        nome = request.form['nome']
        cognome = request.form['cognome']
        password = request.form['password']
        error = None
        tempo = datetime.datetime.now()
        tempo1 = tempo.hour
        tempo2 = tempo.minute
        a = hash1(nome,cognome)
        if a != int(password):
            error = "password non è coretta"
        if not ore:
            error = 'Non hai messo le ore'
        if not minuti:
            error = 'Non hai messo i minuti'
        if not nome:
            error = 'Non hai messo il nome'
        if not cognome:
            error = 'Non hai messo il cognome'
        if not password:
            error = 'Non hai messo la password'
        #if (tempo1 != 19):
            #error = 'Il tempo è scaduto'
        #if (tempo2>40 or tempo2<30):
            #error = 'Il tempo è scaduto'
        if Scomessa.query.filter_by(password = a).first() != None:
            error = 'Hai già inserito'
        if error is None:
            scomessa = Scomessa(ore = ore, minuti = minuti, nome = nome, cognome = cognome, password = a)
            db.session.add(scomessa)
            db.session.commit()
            flash("Dati inseriti corettamente")
            return redirect(url_for('sito'))
        flash(error)
    return render_template('sito.html')
if __name__ == "__main__":
    app.run()




