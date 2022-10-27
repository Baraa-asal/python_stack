from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def show():
    name_on_form=request.form["name"]
    location_on_form=request.form["location"]
    fav_lang_on_form=request.form["fav-lang"]
    comment_on_form=request.form["comment"]
    return render_template("survey.html",name_on_page=name_on_form, location_on_page=location_on_form, fav_lang_on_page=fav_lang_on_form, comment_on_page=comment_on_form)


if __name__ == "__main__":
    app.run(debug=True)