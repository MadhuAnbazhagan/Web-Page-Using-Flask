from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confirm", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        f = request.form.get('fname')
        l = request.form.get('lname')
        g = request.form.get('Gender')
        e = request.form.get('email')
        return  render_template('confirm.html',fname=f,lname=l,Gender=g,email=e)

if __name__ == "__main__":
    app.run(debug=True)