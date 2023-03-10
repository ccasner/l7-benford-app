# L7 Benford App

Challenge 1: Benford's Law. In 1938, Frank Benford published a paper showing the distribution of the leading digit in many disparate sources of data. In all these sets of data, the number 1 was the leading digit about 30% of the time. Benford’s law has been found to apply to population numbers, death rates, lengths of rivers, mathematical distributions given by some power law, and physical constants like atomic weights and specific heats.
Create a python-based web application (use of tornado or flask is fine) that
1) can ingest the attached example file (census_2009b) and any other flat file with a viable target column. Note that other columns in user-submitted files may or may not be the same as the census data file and users are known for submitting files that don't always conform to rigid expectations. How you deal with files that don't conform to the expectations of the application is up to you, but should be reasonable and defensible.
2) validates Benford’s assertion based on the '7_2009' column in the supplied file
3) Outputs back to the user a graph of the observed distribution of numbers with an overlay of the expected distribution of numbers. The output should also inform the user of whether the observed data matches the expected data distribution.

Stretch challenge: The delivered package should contain a docker file that allows us to docker run the application and test the functionality directly.


## Languages and Frameworks
- Python 3.10
- Flask 2.2
- Docker
- Graph images are created using Pandas and Matplotlib libraries

## Application Functionality - Endpoints
### HOME - /
Provides a brief description of Benford's Law sourced from Wikipedia.
### EXAMPLE - /example
A visual example of what to expect after uploading a file. Uses sample data provided in census_2009b.csv file.

### UPLOAD - /upload
Use 'Choose File' button to upload a csv file and include the name of the column which contains the data that the application will use to analyze and compare results. After selecting 'Upload' button, use the 'Show Graph' button to see the results mapped to a bar chart.

### GRAPH - /show_data
A graph of the observed distribution of numbers with an overlay of the expected distribution of numbers.
