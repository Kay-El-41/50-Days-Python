import pandas as pd

#Accessing the website
web = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")

#slicing the list to get table number 1
table = web[1]
print(table)

#getting two column
data_types = table[['Type', 'Mutability']]
print(data_types)