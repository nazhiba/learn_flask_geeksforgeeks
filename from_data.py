from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def student():
     return render_template('student.html')

@app.route('/jawaban', methods=['POST','GET'])
def jawaban():
     if request.method == 'POST':
          jawaban = request.form
          return render_template('jawaban.html', jawaban = jawaban)

if __name__ == "__main__":
     app.run(debug=True)