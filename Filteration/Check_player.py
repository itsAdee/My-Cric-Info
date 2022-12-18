
import pandas as pd

df = pd.read_csv('Playerdatabase.csv')
print(df.loc[df['Scrapped Name'] == "PBB Rajapaksa"]['ID'])
