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
	query = "SELECT * FROM users WHERE email=%s AND password=%s"
	cursor.execute(query, (email, password))
	result=cursor.fetchone()
	# return str(result[0])
	try:
		if result[1]==email and result[2]==password:
			session['loginIn']=True
			return redirect('/welcome')
		else:
			return "invalid user!"
	except Exception as e:
		return redirect('/logout')
	cnx.commit()
@app.route('/welcome')
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


@app.route('/edit')
def edit():
	
app.run(debug=True)






