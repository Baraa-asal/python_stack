from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'counter'

@app.route('/')         
def index():
    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter']+=1
    return render_template("index.html", count= session['counter'])


@app.route('/destroy_session')
def destroy():
    session.pop('counter')
    return redirect('/')



if __name__=="__main__":   
    app.run(debug=True)   