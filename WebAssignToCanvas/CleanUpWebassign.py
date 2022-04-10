import pandas as pd
import numpy as np

# Enter the WebAssign and Canvas csv files
dfWA = pd.read_csv('webassign.csv')
dfC = pd.read_csv('canvas.csv')
#

# Remove homework columns
coldrop = list()
itemrm = ['Homework', 'Student', 'Total', 'Username']

for col in dfWA.columns[1:]:
    for item in dfWA[col]:
        for rm in itemrm:
            if rm in str(item):
                if col not in coldrop:
                    coldrop.append(col)

# All of the columns to remove are stored in coldrop
# Now remove the columns
for col in coldrop:
    dfWA = dfWA.drop([col], axis=1)
#

# Fix the Webassign column titles #
dfWA = dfWA.rename(columns = {dfWA.columns[0]:'Student'})
assign = dfWA.loc[dfWA['Student'] == 'Assignment Name']

assval = assign.values.tolist()[0][1:]

count = 0
for x in assval:
    x = x.strip()
    title = x.split()[2:]
    assval[count] = ''.join(title)
    count = count + 1

for i in range(len(assval)):
    dfWA = dfWA.rename(columns = {dfWA.columns[i+1]:assval[i]})
#

# Turn ND and NS into 0
ndns = ['ND', 'NS']
for col in dfWA.columns[1:]:
    dfWA[col] = dfWA[col].replace(ndns, 0)
#

# Remove rows 0-4 and 6,7 and 35,36 #
# This is specific only for Web Assign Csv files
ind = dfWA.index.values
rowrm = np.concatenate((ind[0:5], ind[6:8], ind[35:37]), axis=None)
dfWA = dfWA.drop(rowrm)
# Reset the index
dfWA = dfWA.reset_index(drop=True)
#

# Remove in inactive students
# Lower case the names of all the studetns.
# Do this because some there will be discrepencies from WA to Canvas

WAstu = list(dfWA[dfWA.columns[0]][1:])
lWAstu = list()
for stu in WAstu:
    low = stu.lower()
    lWAstu.append(low)

Cstu = list(dfC['Student'][1: len(dfC['Student'])-1])
lCstu = list()
for stu in Cstu:
    low = stu.lower()
    lCstu.append(low)

for stu in WAstu:
    low = stu.lower()
    if low not in lCstu:
        dfWA = dfWA.loc[dfWA[dfWA.columns[0]] != stu]
#Reset the index
dfWA = dfWA.reset_index(drop=True)
#

# Add Canvas students who are not on WebAssign
# Set all their scores to 0
length = len(dfWA.iloc[0].values.tolist())

# Function to insert row in the dataframe
# www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
def Insert_row(row_number, df, row_value):
    # Starting value of upper half
    start_upper = 0
    # End value of upper half
    end_upper = row_number
    # Start value of lower half
    start_lower = row_number
    # End value of lower half
    end_lower = df.shape[0]
    # Create a list of upper_half index
    upper_half = [*range(start_upper, end_upper, 1)]
    # Create a list of lower_half index
    lower_half = [*range(start_lower, end_lower, 1)]
    # Increment the value of lower half by 1
    lower_half = [x.__add__(1) for x in lower_half]
    # Combine the two lists
    index_ = upper_half + lower_half
    # Update the index of the dataframe
    df.index = index_
    # Insert a row at the end
    df.loc[row_number] = row_value
    # Sort the index labels
    df = df.sort_index()
    # return the dataframe
    return df

count = 0
for stu in Cstu:
    rowadd = np.zeros(length-1).tolist()
    low = stu.lower()
    if low not in lWAstu:
        rowadd.insert(0, stu)
        dfWA = Insert_row(count+1 , dfWA, rowadd)
    count = count + 1
#

# Store dfWA to a csv file
dfWA.to_csv('webassignCLEAN.csv')
