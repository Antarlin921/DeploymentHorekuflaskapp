# import a library  
from flask import Flask,render_template,request
import joblib

# instace of an app
app=Flask(__name__)

model=joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return "Welcome"

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/welcome')
def welcomepage():
    return render_template("welcome.html")

@app.route('/bologs')
def bologspage():
    return render_template("bologs.html")

@app.route('/blog',methods=['POST'])
def contact():  
    preg= request.form.get('preg')
    plas= request.form.get('plas')
    pres= request.form.get('pres')
    skin= request.form.get('skin')
    test= request.form.get('test')
    mass= request.form.get('mass')
    pedi= request.form.get('pedi')
    age= request.form.get('age')    
    
    print(preg,plas,pres,skin,test,mass,pedi,age)
    
    pred=model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if pred[0]==1:
        output="diabetic"
    else:
        output="Not diabetic"
    return render_template('blog.html',predicted_text=f'The person is {output}')

#  run the app
if __name__=='__main__':
    app.run(debug=True)

