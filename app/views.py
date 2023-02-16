from flask import Flask, render_template, request
import pandas as pd
from . import app




@app.route("/")
def home():
    return render_template("home.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', tables=[data.to_html()], titles=[''])
    return render_template('upload.html')


