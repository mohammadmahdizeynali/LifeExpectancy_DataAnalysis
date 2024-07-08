import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_life_expectancy_by_region(file_path, life_expectancy_col='Life_expectancy', region_col='Region', country_col='Country'):
    
    data = pd.read_csv(file_path)

    sns.set(style="whitegrid")

    regions = data[region_col].unique()

    colors = sns.color_palette("husl", len(regions))
    for i, region in enumerate(regions):
        plt.figure(figsize=(12, 8))
        region_data = data[data[region_col] == region]
        sns.barplot(x=country_col, y=life_expectancy_col, data=region_data, palette=[colors[i]])

        plt.xticks(rotation=90)
        plt.xlabel('Country')
        plt.ylabel('Life Expectancy')
        plt.title(f'Life Expectancy in {region}')
        plt.tight_layout()
        plt.show()

plot_life_expectancy_by_region('/content/primary_dataset.csv')
##########################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_columns_for_region(file_path, region_name='Middle East', region_col='Region', country_col='Country', columns=None):
    if columns is None:
        columns = ['Adult_mortality', 'Infant_deaths', 'GDP_per_capita', 
                   'Population_mln', 'Alcohol_consumption', 'Incidents_HIV']

    data = pd.read_csv(file_path)
    region_data = data[data[region_col] == region_name]
    print(region_data.columns)

    sns.set(style="whitegrid")

    for column in columns:
        if column in region_data.columns:
            plt.figure(figsize=(12, 8))
            sns.barplot(x=country_col, y=column, data=region_data, palette='husl')

            plt.xticks(rotation=90)
            plt.xlabel('Country')
            plt.ylabel(column.replace('_', ' ').title())
            plt.title(f'{column.replace("_", " ").title()} in {region_name}')
            plt.tight_layout()
            plt.show()
        else:
            print(f"Warning: Column '{column}' not found in the dataset for {region_name}.")

plot_columns_for_region('/content/primary_dataset.csv')