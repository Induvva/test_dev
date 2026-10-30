from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def hello_world():
    return '<center><h1>Welcome</h1><a href="/register">Register</a></center>'

@app.route('/success/<user>/<email>/<roll_no>')
def success(user,email,roll_no):
    return render_template('success.html',user=user,email=email,roll_no=roll_no)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_user():
    user=request.form['user']
    email=request.form['email']
    roll_no=request.form['roll_no']
    return redirect(url_for('success',user=user,email=email,roll_no=roll_no))

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)