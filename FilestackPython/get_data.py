import requests
import json
import boto3

s3 = boto3.resource('s3')

url = "https://classic.clinicaltrials.gov/api/query/full_studies?expr=AREA%5bLeadSponsorName%5dGilead%20OR%20AREA%5bCollaboratorName%5dGilead&min_rnk=1&max_rnk=100&ALL=all&fmt=json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    clean_data = json.dumps(data, indent=4)
    
    file_path = 'url_data.json'
    with open(file_path, 'w') as json_file:
        json_file.write(clean_data)
    s3.meta.client.upload_file(r'C:\Users\Zoroa\OneDrive\Documents\Python for Anything\FilestackPython\url_data.json', 'zoroarctestbucket', 'CSdata.json')
else:
    print('Error fetching data')