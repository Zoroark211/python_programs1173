import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('CTDataTable.xlsx')

# Convert the column name 'BN' to its corresponding index
column_bn_index = pd.Series(df.columns).str.match('BN').idxmax()

print("The index of column BN is:", column_bn_index)
