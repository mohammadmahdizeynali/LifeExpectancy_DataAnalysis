# In the name of God

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

file_path = "E:\\LifeExpectancy_DataAnalysis\\primary_dataset.csv"

data = pd.read_csv(file_path)

print(data.head())

#hist
def plot_histogram(data, variables):
    colors = ['skyblue', 'salmon', 'mediumseagreen', 'gold', 'tomato', 'teal', 'violet', 'lightcoral', 'royalblue', 'orange', 'slategray', 'darkorchid', 'indianred', 'forestgreen']  # لیست رنگها برای هر متغیر
    
    for i, var in enumerate(variables):
        plt.figure(figsize=(8, 6))
        plt.hist(data[var].dropna(), bins=20, color=colors[i % len(colors)])
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.show()

variables = ['Infant_deaths', 'Under_five_deaths', 'Adult_mortality', 'Alcohol_consumption', 'Hepatitis_B', 'Measles',
             'BMI', 'Diphtheria', 'GDP_per_capita', 'Population_mln', 'Thinness_ten_nineteen_years', 'Thinness_five_nine_years', 'Schooling', 'Life_expectancy']

plot_histogram(data, variables)

#scatter
def scatter_plot(data, x_variable):
    variables = ['Infant_deaths', 'Under_five_deaths', 'Alcohol_consumption', 'GDP_per_capita', 'Population_mln','Adult_mortality']
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']  
    
    for i, variable in enumerate(variables):
        plt.figure(figsize=(8, 6))
        plt.scatter(data[x_variable], data[variable], color=colors[i]) 
        plt.title(f'Scatter Plot of {x_variable} vs. {variable}')
        plt.xlabel(x_variable)
        plt.ylabel(variable)
        plt.grid(True)
        plt.show()

scatter_plot(data, 'Life_expectancy')

#box_plot
def box_plot(data, x_variable, y_variable):
    plt.figure(figsize=(12, 8))  
    sns.boxplot(x=x_variable, y=y_variable, data=data, palette='Set3')  
    plt.title(f'Box Plot of {y_variable} by {x_variable}')
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.xticks(rotation=45)  
    plt.grid(True)
    plt.show()


X_variables = ['Economy_status_Developing', 'Region']

for var in X_variables:
    box_plot(data, var, 'Life_expectancy')

# region_LE
data['Life_expectancy'].dtype

data_grouped_by_region = data.groupby('Region')['Life_expectancy'].mean().reset_index()
data_grouped_by_region = data_grouped_by_region.rename(columns={'Life_Expectancy': 'mean_life_expectancy'})
data_grouped_by_region.head()

#plot_bar_chart
def plot_bar_chart(data):
    plt.figure(figsize=(12, 6))
    plt.bar(data['Region'], data['Life_expectancy'], color='skyblue')
    plt.xlabel('Region')
    plt.ylabel('Mean Life Expectancy')
    plt.title('Mean Life Expectancy by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_bar_chart(data_grouped_by_region)

#calculate_mean
def calculate_mean(data):
    mean_data = data.groupby('Region')['Life_expectancy'].mean().reset_index()
    return mean_data

mean_life_expectancy_by_region = calculate_mean(data)
data_grouped.head(20)

#line_chart
def plot_line_chart(data):
    plt.figure(figsize=(12, 6))
    for region in data['Region'].unique():
        region_data = data[data['Region'] == region]
        plt.plot(region_data['Year'], region_data['Life_expectancy'], label=region)

    plt.xlabel('Year')
    plt.ylabel('Mean Life Expectancy')
    plt.title('Mean Life Expectancy by Region over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


plot_line_chart(data_grouped)