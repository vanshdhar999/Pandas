import pandas as pd
# indexing in pandas

# works more or less like accessing a series from a dataframe. 
oscar_male_age = pd.read_csv('../files/oscar_age_male.csv', index_col = 0)
# think of it like a dictionary 

#file_name['Column_name'] --> gives the list of the column 

# Indexing in pandas?
#We can use iloc function to get the required row with indexed columns.
print(oscar_male_age.iloc[:, 0])

# : operator means everything just like in python. We can specify the range of the 
# columns we want to select.
print(oscar_male_age.head())
print(oscar_male_age.iloc[0:3, 4])

# It's also possible to pass a list:

# Using loc operator is conceptually difficult than iloc.




# manipulating the index 
# We can index the data as we like.

oscar_male_age.set_index("Age")

# Conditional indexing. Sometimes it is useful to retrieve data with certain conditions.


# Conditional operators.

oscar_male_age.loc[oscar_male_age.Name == "Vansh"]

oscar_male_age.loc[(oscar_male_age.Name == "Robert DeNiro") & (oscar_male_age.Index == 1293)]

# We can use & operator or | operator as we like.


# isin operator lets you select values in the given list of values.


oscar_male_age.loc[oscar_male_age.Name.isin(["Leo", "Robert"])]

# isnull and notnull operator lets you find the values wihch are not there or are there.

oscar_male_age.loc[oscar_male_age.Name.isnull()] # or notnull

# assinging data is easy

oscar_male_age['Name'] = "John Doe"

oscar_male_age['index_backwards'] = range(len(oscar_male_age), 0, -1) # indexs backwards

