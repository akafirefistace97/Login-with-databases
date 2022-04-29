from flask import Flask, render_template, redirect,session,request
import mysql.connector

#connection to databases
conn=mysql.connector.connect(user='root',password='',host='localhost',database='python')

cursor=conn.cursor()

app=Flask(__name__)
app.secret_key="pushpa"

@app.route('/')
@app.route('/login')

def login():
	return render_template('login.html')

@app.route('/check', methods=['post'])
def check():
	email=request.form['email']
	password=request.form['password']
	if email==request.form['email'] and password==request.form['password']:
		session['loginIn']=True
		return redirect('/welecome')
	else:
		return redirect("invalid user!")
@app.route('/welecome')
def welcome():
	query = "SELECT users.*, colleges.college_name FROM users INNER JOIN colleges ON users.college_id = colleges.id"
	cursor.execute(query)
	result = cursor.fetchall()
	conn.commit()
	try:
		if session['loginIn']==True:
			return render_template('/welecome.html',result=result)
	except Exception as e:
		return redirect('/login')


@app.route('/logout')
def logout():
	try:
		session.pop('loginIn')
		return redirect('/login')
	except Exception as e:
		return redirect('/login')



app.run(debug=True)