from flask import Flask, render_template
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')

# dynamic route: http://localhost:5000/user/name
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)