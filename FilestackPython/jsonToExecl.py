import pandas as pd
import json

with open('CTdata.json') as file:
    data = json.load(file)

fullStudiesData = data["FullStudiesResponse"]["FullStudies"]

normalized = pd.json_normalize(fullStudiesData)

dataFrame = pd.DataFrame(normalized)

excelFile = 'CTDataTable.xlsx'
dataFrame.to_excel(excelFile, index=False)