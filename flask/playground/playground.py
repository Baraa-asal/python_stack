from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def welcome():
    return render_template('index.html', colour='pink', x=15)


@app.route('/play/<int:x>/<colour>')
def play(x, colour):
    return render_template("index.html", x=x, colour=colour)


if __name__ == "__main__":
    app.run(debug=True)
