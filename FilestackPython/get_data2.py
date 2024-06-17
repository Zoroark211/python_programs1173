import boto3
import requests
import json

def fetch_website_data(url):
    response = requests.get(url)
    return response.json()

def upload_json_to_s3(data, bucket_name, key):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data, indent=4))

website_url = "https://classic.clinicaltrials.gov/api/query/full_studies?expr=AREA%5bLeadSponsorName%5dGilead%20OR%20AREA%5bCollaboratorName%5dGilead&min_rnk=1&max_rnk=100&ALL=all&fmt=json"

bucket_name = "zoroarctestbucket"
object_key = "CTdata.json"

json_data = fetch_website_data(website_url)

upload_json_to_s3(json_data, bucket_name, object_key)