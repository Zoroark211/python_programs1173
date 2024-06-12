import requests
import json

url = "https://classic.clinicaltrials.gov/api/query/full_studies?expr=AREA%5bLeadSponsorName%5dGilead%20OR%20AREA%5bCollaboratorName%5dGilead&min_rnk=1&max_rnk=100&ALL=all&fmt=json"

response = requests.get(url)
data = response.json()

json_str = json.dumps(data, indent=4)

file_path = "url_data.json"

with open(file_path, "w") as json_file:
    json_file.write(json_str)

print("JSON data has been saved to:", file_path)