import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_pairplot(df):
    sns.pairplot(df)
    plt.show()

df = pd.read_csv('/content/primary_dataset.csv')
plot_pairplot(df)