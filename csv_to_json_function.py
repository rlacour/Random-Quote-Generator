import csv
import json
import os

os.chdir('C:\\Users\\lacou\\Documents\\Little Red Quote Generator')
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:

            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows

    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# My filepath for the csv and
# path decided for new json file
csvFilePath = 'Source Quotes Ch 1-3.csv'
jsonFilePath = 'Source Quotes Ch 1-3.json'

# apply the function
make_json(csvFilePath, jsonFilePath)

# function template found at
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
