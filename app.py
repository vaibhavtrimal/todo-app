from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    datee=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno}-{self.title}"
    

@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.route('/products')
# def products():
#     # return 'this is products page'
#     # return /templates/index.html
#     return render_template("index.html")

@app.route('/features')
def products():
    return render_template("features.html")

@app.route('/todo',methods=['GET','POST'])
def todo():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo=Todo.query.all()
    # print(alltodo)
    # pass the alltodo to todo.html with alltodo name
    return render_template("todo.html",alltodo=alltodo)


@app.route('/delete/<int:sno>')
def delete(sno):
    de=Todo.query.filter_by(sno=sno).first()
    db.session.delete(de)
    db.session.commit()
    return redirect('/todo')
    

if __name__=="__main__":
    app.run(debug=True)

