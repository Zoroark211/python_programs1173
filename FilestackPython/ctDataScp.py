import pandas as pd
import json
import ast

excelFile = pd.read_excel('CTDataTable.xlsx')
cellData = excelFile.iat[1, 63]

# data1 = json.dumps(cellData)
print(cellData)
print(type(cellData))

# editData = cellData[1:-1] # type tuple
# changedData = json.loads(data1) # type str?
changedData = eval(cellData) # type list
# changedData = ast.literal_eval(cellData) #type: list

print(changedData)
print(type(changedData))

dataFrame = pd.DataFrame(changedData)
'''
newExcelFile = 'NCT06374758.xlsx'
dataFrame.to_excel(newExcelFile, index=False)
'''

print(dataFrame)