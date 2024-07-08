import pandas as pd

def compute_numeric_correlation(file_path):
    
    df=pd.read_csv(file_path) 
    
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns

    df_numeric = df.drop(non_numeric_cols, axis=1)

    return df_numeric.corr().head()

file_path = 'primary_dataset.csv' 
result = compute_numeric_correlation(file_path)