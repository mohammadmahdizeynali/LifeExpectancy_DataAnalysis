import pandas as pd

file_path = "E:\\LifeExpectancy_DataAnalysis\\primary_dataset.csv"

df2 = pd.read_csv(file_path)

print(df2.head())

from sklearn.preprocessing import StandardScaler

#unnormal feature
non_normal_features = ['Infant_deaths', 'Under_five_deaths', 'Adult_mortality', 'Alcohol_consumption',
                       'Hepatitis_B', 'Measles', 'BMI', 'Polio', 'Diphtheria',
                       'Incidents_HIV', 'GDP_per_capita', 'Population_mln',
                       'Thinness_ten_nineteen_years', 'Thinness_five_nine_years',
                       'Schooling', 'Life_expectancy']

scaler = StandardScaler()

df2[non_normal_features] = scaler.fit_transform(df2[non_normal_features])
print(df2[non_normal_features])