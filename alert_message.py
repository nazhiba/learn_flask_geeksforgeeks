from flask import Flask, render_template, redirect, url_for, request, flash
app = Flask(__name__)

@app.route('/login', methods = ['GET','POST'])
def login():
     error = None
     if request.method == "POST":
          if request.form['username'] != 'admin' or request.form['password'] != 'admin':
               error = "invalid username or password. try again!"
               print(error)
          else:
               # flash('kamu berhasil login')
               return render_template('index_alert_message.html')
     return render_template('login.html', error=error)


if __name__ == "__main__":
     app.run(debug=True)