from flask import(
    Flask,
    render_template,
    request,

)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html',)

@app.route('/log')
def log():
    return render_template('login.html',)

@app.route('/about')
def about():
    return render_template('about.html',)

if __name__ == '__main__':
    app.run(debug=True)