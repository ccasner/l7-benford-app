import csv
import os
from flask import render_template, request
import pandas as pd

from app.show_graph import CreateGraph
from . import app

UPLOAD_FOLDER = 'app/static/files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/example")
def example():
    return render_template("example.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        column = request.form['text']
        
        try:
            uploaded_file = request.files.get('file')
            if uploaded_file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(file_path)

                with open(file_path, newline='') as csvfile:
                    dialect = csv.Sniffer().sniff(csvfile.readline())
                    csvfile.seek(0)
                    data = pd.read_csv(file_path, usecols=[column], sep=dialect.delimiter, engine='python')
                    CreateGraph(data, column).process_data()

        except ValueError:
            message = 'Column not found, please try again'
            return render_template('upload_error.html', message=message)

        return render_template('upload.html', tables=[data.to_html()], titles=[''])
    return render_template('upload.html')


@app.route('/show_data')
def show_data():

    image = '/static/images/plot.png'

    return render_template('show_data.html', url=image)



if __name__ == "__main__":
    app.run(debug=True)
