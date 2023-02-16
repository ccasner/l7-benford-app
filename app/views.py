from flask import Flask, render_template, request
import pandas as pd
from . import app

# col_to_sort = '7_2009'

# ## TODO: add input validation for column name 
# df = pd.read_csv('example.csv', sep = '\t', usecols=[col_to_sort])

# list_of_firsts = []
# for num in df[col_to_sort].values:
#     # convert num to str to get first digit, return as int
#     first_num = int(str(num)[0])
#     # add digits to list of all firsts
#     list_of_firsts.append(first_num)

# # convert list to pandas series
# sr = pd.Series(list_of_firsts)
# # Print the series
# print(sr)
# # Print the value counts for each digit in the series
# print(sr.value_counts())
  




# if df.columns.values.__contains__(col_to_sort):
#     for x in df.columns[2]:
#         col_values = df[col_to_sort]

# df.to_html('example.html')

@app.route("/")
def home():
    return render_template("home.html")


# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         data = pd.read_csv(request.files.get('file'), sep='\t')
#         return render_template('upload.html', tables=[data.to_html()], titles=[''])
#     return render_template('upload.html')


@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    if request.method == 'POST':

        col_to_sort = '7_2009'
        data = pd.read_csv(request.files.get('file'), sep='\t', usecols=[col_to_sort])

        list_of_firsts = []
        for num in data[col_to_sort].values:
            # convert num to str to get first digit, return as int
            first_num = int(str(num)[0])
            # add digits to list of all firsts
            list_of_firsts.append(first_num)

        # convert list to pandas series
        sr = pd.Series(list_of_firsts)
        # Print the series
        print(sr)
        # Print the value counts for each digit in the series
        print(sr.value_counts())
        sr_counts = sr.value_counts()
        data = sr_counts.to_frame()

        return render_template('show_data.html', tables=[data.to_html()], titles=[''])
    return render_template('show_data.html')

