from flask import Flask
app = Flask(__name__)

def show_users(username):
     return f'Hallo {username}'

app.add_url_rule('/users/<username>', view_func=show_users, methods=['POST','GET'])

if __name__ == "__main__":
     app.run(debug=True)