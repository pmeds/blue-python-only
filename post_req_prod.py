import csv
import json
import requests
import sys
import warnings

#warnings.filterwarnings('ignore', message='Unverified HTTPS request')
# Check if argument was passed. If no argument was passed then don't do anything.
# Ideally this scenario should not happen because there is a pre-check on Jenkins to see if the files exists.

if len(sys.argv) < 2:
    print('No file provided, no rules to upload')
    exit()
else:
    file_name = sys.argv[1]

if file_name:
    reader = csv.DictReader(open(file_name))
    # Iterate over the rows
    for row in reader:
        # Convert the row to a JSON string
        json_data = json.dumps(row)
        print(json_data)
        # Define the POST request's URL
        url = 'https://paulm-sony.test.edgekey.net/upload'
        # Define the POST request's headers
        headers = {"Content-type": "application/json", "Host": "paulm-sony.test.edgekey.net"}
        # Make the POST request
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url, data=json_data, headers=headers, verify=False)
        # Print the response
        rheaders = response.headers
        rresponse = response.status_code
        print(rresponse, rheaders)
