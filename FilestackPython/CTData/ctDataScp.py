import pandas as pd

excelFile = pd.read_excel('CTDataTable.xlsx')
newExcelFile = 'CTDataSpcBN.xlsx'

idColumnIndex = 1
cellColumnIndex = 65

appendDataFrame = []

for i in range(len(excelFile)):
    idValue = excelFile.iat[i, idColumnIndex]
    cellData = excelFile.iat[i, cellColumnIndex]

    if pd.notna(cellData):
        try:
            changedData = eval(cellData)
            dataFrame = pd.DataFrame(changedData)
            dataFrame.insert(0, excelFile.columns[idColumnIndex], idValue)
#            print(dataFrame)
            appendDataFrame.append(dataFrame)
        except Exception as e:
            print(f'Error with data in cell BN for ID {idValue}: {e}')
    else:
        print(f'Column BN is empty for ID {idValue}.')

combined = pd.concat(appendDataFrame, ignore_index=True)
combined.to_excel(newExcelFile, index=False)