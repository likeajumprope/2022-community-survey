import pandas as pd
import seaborn as sns

df = pd.read_csv('public_survey_data.csv', sep=',', index_col='Unnamed: 0', header=0)

# Print the unique answers to input questions
print(
    df['What geographic region are you currently located in?'].unique(),
    df['What is your current career status?'].unique()
)

df.info()
print(df.head())

print(df["Are you a member of OHBM?"].value_counts(normalize=True) * 100)

