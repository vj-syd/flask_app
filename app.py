from flask import Flask, redirect, url_for, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/form')
def form():
    return render_template('form.html')
 

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('index.html',form_data = form_data)


if __name__ == "__main__":
    app.run()
