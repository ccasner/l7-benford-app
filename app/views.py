from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from . import app


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
        # create_graph()

        return render_template('show_data.html', tables=[data.to_html()], titles=[''])
    return render_template('show_data.html')


# Returns pandas series containing actual counts for each leading digit
def get_actual_counts():

    col_to_sort = '7_2009'

    df = pd.read_csv('sample_data.csv', sep = '\t', usecols=[col_to_sort])

    list_of_firsts = []
    for num in df[col_to_sort].values:
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
    sr_counts = sr.value_counts()[:9]
    # data = sr_counts.to_frame()

    data = sr.value_counts()[:9]

    return data


# Returns array of expected counts based on Benford's law 
def get_expected_counts():

    col_to_sort = '7_2009'

    df = pd.read_csv('sample_data.csv', sep = '\t', usecols=[col_to_sort])
    print(df.size)

    benford_percentages = [.301, .176, .125, .097, .079, .067, .058, .051, .046]
    print('BEFORE: ', benford_percentages)
    benford_results = [i * df.size for i in benford_percentages]
    print('AFTER: ', benford_results)

    return benford_results


# Create bar graph comparing results 
benford = get_expected_counts()
actual = get_actual_counts()
# index = [1,2,3,4,5,6,7,8,9]

plotdata = pd.DataFrame({

    "Benford": benford,

    "Actual": actual})

plotdata.plot(kind="bar",figsize=(15, 8))
plt.show()

