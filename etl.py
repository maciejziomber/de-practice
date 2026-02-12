import pandas as pd
import json

#Extract
df = pd.read_csv('data/raw_data.csv')

#Transform
df['city '] = df['city '].str.upper()

#Load (save as Json)
df.to_json('data/processed_data.json', orient='records', indent=4)
print("Data Engineering pipeline complete!")