import json
import pandas as pd

with open('cars1.json', 'r') as file:
    data1 = json.load(file)

with open('cars2.json', 'r') as file:
    data2 = json.load(file)

with open('cars3.json', 'r') as file:
    data3 = json.load(file)

combined = {
    'carsC': data1['cars'] + data2['cars'] + data3['cars']
}

'''
jsonData = json.dumps(combined, indent=4)

print(combined)
'''
dataFrame = pd.DataFrame(combined['carsC'])

excelFile = 'carTable3.xlsx'
dataFrame.to_excel(excelFile, index=False)