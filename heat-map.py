import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_correlation_heatmap(df_numeric):
    
    
    numeric_columns = df_numeric.select_dtypes(include=['number'])
    correlation_matrix = numeric_columns.corr()
    
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()


df = pd.read_csv('/content/primary_dataset.csv')
plot_correlation_heatmap(df) 