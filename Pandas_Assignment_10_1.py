import pandas as pd

#Read dataset
us_baby=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

print('Top 5 Rows before deleting unnamed columns\n','-'*30)
print(us_baby.head())
print('\nTop 5 Rows after Delete unnamed columns\n','-'*30)

print(us_baby.drop(columns='Unnamed: 0').head())

print('\nShow the distribution of male and female\n','-'*40)
print(us_baby.groupby('Gender').Count.sum())

print('\nShow the top 5 most preferred names\n','-'*40)
print(us_baby.groupby('Name').sum().sort_values('Count',ascending=False).head())

print('\nWhat is the median name occurence in the dataset\n','-'*50)
print(us_baby.groupby('Name').Count.mean().sort_values(ascending=False).head(1))

print('\nDistribution of male and female born count by states\n','-'*50)
print(us_baby.groupby(['Gender','State']).Count.sum().to_string())