import csv
from flask import render_template, request
import pandas as pd

from app.show_graph import CreateGraph
from . import app


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
                uploaded_file.save(uploaded_file.filename)
        
            with open(uploaded_file.filename, newline='') as csvfile:
                dialect = csv.Sniffer().sniff(csvfile.readline())
                csvfile.seek(0)
                data = pd.read_csv(uploaded_file.filename, usecols=[column], sep=dialect.delimiter, engine='python')
                # CreateGraph(data, column).create_graph_image()
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
