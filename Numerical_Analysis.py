import pandas as pd

file_path = "E:\\LifeExpectancy_DataAnalysis\\primary_dataset.csv"

data = pd.read_csv(file_path)

print(data.head())


#info_data
def info_data(data):
     return(data.info())

info_data(data)

#describe_data
def describe_data(data):
    return data.describe()
    
describe_data(data)


#check_normality
from scipy.stats import shapiro
def check_normality(data):
    variables = ['Infant_deaths','Year', 'Under_five_deaths', 'Adult_mortality', 'Alcohol_consumption', 'Hepatitis_B', 
                 'Measles', 'BMI', 'Polio', 'Diphtheria', 'Incidents_HIV', 'GDP_per_capita', 'Population_mln', 
                 'Thinness_ten_nineteen_years', 'Thinness_five_nine_years', 'Schooling', 'Life_expectancy']

    for var in variables:
        stat, p = shapiro(data[var])
        print(f'Variable: {var}')
        print(f'Statistic: {stat}, p-value: {p}')

        if p > 0.05:
            print('Normal distribution: Yes\n')
        else:
            print('Normal distribution: No\n')

check_normality(data)

