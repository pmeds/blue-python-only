import csv
import json
import requests
import sys

# Check if argument was passed. If no argument was passed then don't do anything.
# Ideally this scenario should not happen because there is a pre-check on Jenkins to see if the files exists.

if len(sys.argv) < 2:
    print('No file provided, no rules to upload')
else:
    file_name = sys.argv[1]

    if file_name:
        f = file_name
        print(f)
        with open(f, 'r') as file:
            # Read the CSV file
            reader = csv.DictReader(file)
            # Iterate over the rows
            for row in reader:
                # Convert the row to a JSON string
                json_data = json.dumps(row)
                print(json_data)
                # Define the POST request's URL
                url = 'https://paulm-sony.test.edgekey.net/upload'
                # Define the POST request's headers
                headers = {"Content-type": "application/json"}
                # Make the POST request
                response = requests.post(url, data=json_data, headers=headers)
                # Print the response
                print(response.text)
    else:
        print('File not found, no rules to upload')