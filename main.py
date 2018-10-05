from flask import Flask, request, redirect, render_template
import cgi
import sys


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def main():
    
    if request.method == "GET":
        error = {}
        return render_template('index.html', error=error)

    if request.method == "POST":
        error = {}
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password'] 
        email = request.form['email']      
        
        if len(username) == 0:
            error['username'] = "Please provide a username" 
        elif not (len(username) < 3 or len(username) < 20):
            error['username'] = "Invalid Username"

        if len(password) == 0:
            error['password'] = "Please provide a password"
        elif not (len(password) < 3 or len(password) < 20):
            error['password'] = "Invalid Password"

        if len(verify_password) == 0:
            error['verify_password'] = "Please confirm your password"  
        if password != verify_password:
            error['verify_password'] = "Password Doesn't Match"

        if len(email) == 0:
            error['email'] = "Please provide an email address"  
        elif not (len(email) < 3 or len(email)  < 20):
            error['email'] ="Invalid email name"

        if email.count('.') != 1:
            error['email'] = "Please provide an email address"
                  
        if email.count('@')  != 1:
            error['email'] = "Please provide an email address" 
          
        
        print(error, file=sys.stderr)

        if not error:
            username = username
            return redirect('/welcome?username={0}'.format(username))
        else:              
            return render_template('index.html', 
            error=error,
            username=username,
            email=email)
     
@app.route('/welcome')
def did_signup ():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)  
app.run() 
