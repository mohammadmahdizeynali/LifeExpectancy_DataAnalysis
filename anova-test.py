import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def perform_anova(df, dependent_var, independent_var, alpha=0.05):
    
    dependent_data = df[dependent_var]
    independent_data = df[independent_var]

    data = pd.DataFrame({dependent_var: dependent_data, independent_var: independent_data})

    model = ols(f'{dependent_var} ~ C({independent_var})', data=data).fit()

    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)

    p_value = anova_table["PR(>F)"][0]

    if p_value < alpha:
        print("P-value is less than alpha. Reject the null hypothesis that means are equal.")
    else:
        print("Fail to reject the null hypothesis. Means are not significantly different.")

df = pd.read_csv('/content/primary_dataset.csv')
perform_anova(df, 'Life_expectancy', 'Region')