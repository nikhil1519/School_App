from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20),  nullable=False)
    lname = db.Column(db.String(20),  nullable=False)
    dob = db.Column(db.String(10),  nullable=False)
    father = db.Column(db.String(20),  nullable=False)
    adds = db.Column(db.String(2000),  nullable=False)
    city = db.Column(db.String(20),  nullable=False)
    phone = db.Column(db.Integer,  nullable=False)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.fname} - {self.lname}'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        dob = request.form.get('dob')
        father = request.form.get('father')
        adds = request.form.get('adds')
        city = request.form.get('city')
        phone = request.form.get('phone')

        data = Data(fname = fname, lname=lname, dob = dob, father = father, adds = adds, city = city, phone = phone)
        db.session.add(data)
        db.session.commit()
    alldata = Data.query.all()
    return render_template('hello.html', alldata=alldata)

# @app.route('/')
# def products():
#     return 'this is products page.'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        dob = request.form.get('dob')
        father = request.form.get('father')
        adds = request.form.get('adds')
        city = request.form.get('city')
        phone = request.form.get('phone')

        data = Data.query.filter_by(sno=sno).first()
        data.fname = fname
        data.lname = lname
        data.dob = dob
        data.father = father
        data.adds = adds
        data.city = city
        data.phone = phone
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    data = Data.query.filter_by(sno=sno).first()
    return render_template('update.html', data=data)

@app.route('/delete/<int:sno>')
def delete(sno):
    data = Data.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()


