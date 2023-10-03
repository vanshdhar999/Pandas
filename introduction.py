#import package 
import pandas as pd

# There are two core subjects in pandas: DataFrame and Series

# A dataframe is like a table. The syntax for the dataframe is like the dictionary
table = pd.DataFrame({'Name':['Vansh','Shaleen'], 'Surname':['Dhar','Gupta']})


#the indexing of the rows by default is done as 0,1,2..... But we can change it as we like
# Using index attribute.

table = pd.DataFrame({'Name':['Vansh','Shaleen'], 'Surname':['Dhar','Gupta']}, index = ['Name 1', 'Name 2'])


# A series by contrast is a list or sequence of the items. We can define it as a sequence.

table = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


# How to read data from the files.

oscar_male_age = pd.read_csv('./oscar_age_male.csv')
#print(oscar_male_age)

# We can use the shape command to find the rows and columns of the dataset.

oscar_male_age.shape

# We can preview the data set using the head command.

oscar_male_age.head()

