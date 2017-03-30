# -*- coding: utf-8 -*-
"""
Numpy, Pandas, and Matplotlib learning with "Supermarket Transactions.xlsx"
For CP2403 - Data Visualisation and Modelling
JCU Cairns 

Using Spyder3 IDE (Python 3.6 (Anaconda))
@author: Steven Williams - swill215
@date: 29-30 March 2017
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Import Excel sheet
xl = pd.ExcelFile("Supermarket Transactions.xlsx")
print(xl.sheet_names)

# Define specific workbook sheet
df = xl.parse("Data")
print(df[0:3])

location = df.ix[:,"City":"Country"]
print(location[0:6])

# Get all of the states, and count the total number of times the state is stated
counter = []
states = []
for state in df.ix[:,"State or Province"]:
    i = 0
    if state in states:
        for place in states:
            if place == state:
                counter[i] += 1
            i += 1
    else:
        states.append(state)
        counter.append(1)

# length of dataframe
count = []
for i in range(len(states)):
    count.append(i)


# Determine based on date (year)
i = 0
for date in df.ix[:,"Purchase Date"]:
    d = np.array([date], dtype="datetime64")
    if "2012" in str(d[0]):
        i += 1
print("\nNumber of entries for year 2012: {}".format(i))

# Data related to CA. 
df2 = df.loc[df["State or Province"] == "CA"]

# Total revenue of CA. 
total_revenue = 0
for revenue in df2.ix[:,"Revenue"]:
    total_revenue += float(revenue)
print("\nTotal Revenue of CA: ${}".format(total_revenue))

# Get revenue data
# for revenue in df.ix[:,"Revenue"]:
#    print(revenue)


# Main plot
"""
# Custom labels
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

# Bar graph
ax1.bar(count, counter, label="Values")

# Display graph
plt.xlabel("City")
plt.ylabel("Count")
plt.title("The number of times a city is print")
plt.legend()
plt.show()
"""
