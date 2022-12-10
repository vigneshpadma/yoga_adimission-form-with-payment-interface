import flask
from flask import render_template,request,Flask
import mysql.connector
import smtplib

app=Flask(__name__)

mydb=mysql.connector.connect(host="localhost",port='3306',user="root",password="password",database="yogaform",auth_plugin='mysql_native_password')

my_cursor=mydb.cursor()


@app.route('/')
def register():
    return render_template("admission.html")

@app.route('/',methods=['POST'])
def admission():
    name=request.form['name']
    age=request.form['age']
    email=request.form['email']
    global email
    phoneNumber=request.form['phno']
    batch=request.form['batch']
    password=request.form['psw']
    my_cursor.execute("""insert into 'student'('name','age','email','phoneNumber','batch')values('{}','{}','{}','{}','{}')""".format(name,age,email.phoneNumber,batch))
    mydb.commit()
    return render_template("payment.html")

@app.route('/',methods=['POST'])
def payment():
    paymentType=request.form['payment_type']
    if payment is None:
        if paymentType=='upi':
            upiid=request.form['upiid']
        elif paymentType=='ccard':
            cardNumber=request.form['card_number']
            exp_date=request.form['expiry_date']
            ccv=request.form['ccv']
    else:
        return 'registered successfully'

@app.route('/')
def paymentComplete():
    if payment is not None:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("classicyoga@gmail.com",email)
        message = "payment completed "
        s.sendmail("classicyoga@gmail.com", email, message)
        s.quit()
    
    
if __name__=="__main__":
    app.run(debug=True)
