from flask import Flask

app = Flask(__name__) 

@app.route('/')
def welcome():
    return "welcome to page"

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<name>')
def sayhi(name):
    return f"Hi {name}"      #formatting

@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    return (name+ ' ')*num

if __name__ == "__main__":
    app.run(debug=True)