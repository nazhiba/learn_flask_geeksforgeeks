from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookies', methods=['POST', 'GET'])
def setcookies():
    if request.method == "POST":
        user = request.form['name']
        resp = make_response(render_template('cookie.html'))
        resp.set_cookie('userID', user)  # perbaikan: set_cookie tanpa 's'
        return resp

@app.route('/getcookies')
def getcookies():
    name = request.cookies.get('userID')
    if name:
        return f'<h1>Welcome {name}</h1>'
    else:
        return '<h1>Cookie not set yet!</h1>'  # Tanggapan jika cookie belum ada

if __name__ == "__main__":
    app.run(debug=True)
