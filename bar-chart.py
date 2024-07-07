import pandas as pd
import matplotlib.pyplot as plt

def plot_avg_life_expectancy(file_path):

    df = pd.read_csv(file_path)

    avg_life_expectancy = df.groupby('Country')['Life_expectancy'].mean().reset_index()

    plt.figure(figsize=(25, 16))
    plt.bar(avg_life_expectancy['Country'], avg_life_expectancy['Life_expectancy'], color='skyblue')
    plt.xlabel('Countries')
    plt.ylabel('Average Life Expectancy')
    plt.title('Average Life Expectancy across Different Countries')
    plt.xticks(rotation=90)  

    plt.tight_layout()
    plt.show()

file_path = '/content/primary_dataset.csv'
plot_avg_life_expectancy(file_path)
##########################################

def plot_avg_gdp_per_capita(file_path):

    df = pd.read_csv(file_path)

    avg_gdp_per_capita = df.groupby('Country')['GDP_per_capita'].mean().reset_index()

    plt.figure(figsize=(25, 16))
    plt.bar(avg_gdp_per_capita['Country'], avg_gdp_per_capita['GDP_per_capita'], color='orange')
    plt.xlabel('Countries')
    plt.ylabel('Average GDP per Capita')
    plt.title('Average GDP per Capita across Different Countries')
    plt.xticks(rotation=90)  # چرخش نام کشورها برای بهتر دیده شدن

    plt.tight_layout()
    plt.show()

plot_avg_gdp_per_capita(file_path)