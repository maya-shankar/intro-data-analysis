import pandas as pd

life_expectancy = pd.read_csv('life_expectancy.csv')
print len(life_expectancy['Country'].unique())