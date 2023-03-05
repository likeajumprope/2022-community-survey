import pandas as pd

df = pd.read_csv('public_survey_data.csv', sep=',', index_col='Unnamed: 0')

# Print the unique answers to input questions
print(
    df['What geographic region are you currently located in?'].unique(),
    df['What is your current career status?'].unique()
)