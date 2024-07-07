import pandas as pd
from scipy import stats

def perform_ttest(df, group_col, target_col, group1_value, group2_value, alpha=0.05):

    group1 = df[df[group_col] == group1_value][target_col]
    group2 = df[df[group_col] == group2_value][target_col]

    t_statistic, p_value = stats.ttest_ind(group1, group2)

    print('t-test results:')
    print('----------------------')
    print('Group 1:')
    print('Sample size:', len(group1))
    print('Mean:', group1.mean())
    print('Variance:', group1.var())
    print()
    print('Group 2:')
    print('Sample size:', len(group2))
    print('Mean:', group2.mean())
    print('Variance:', group2.var())
    print()
    print('t-statistic:', t_statistic)
    print('p-value:', p_value)

    print()
    alpha = 0.05
    if p_value < alpha:
        print('Conclusion: The mean life expectancy between the two groups is statistically significantly different.')
    else:
        print('Conclusion: The mean life expectancy between the two groups is not statistically significantly different.')

df = pd.read_csv('/content/primary_dataset.csv')
perform_ttest(df, 'Economy_status_Developed', 'Life_expectancy', 1, 0)