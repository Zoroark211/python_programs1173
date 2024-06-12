import pandas as pd

dataFrame = pd.read_excel('CTDataTable.xlsx')

count = dataFrame['Study.ProtocolSection.IdentificationModule.NCTId'].nunique()
id = dataFrame['Study.ProtocolSection.IdentificationModule.NCTId'].value_counts()

print('Number of Unique IDs in CTData: ', count)
print('List of Unique IDs ', id)