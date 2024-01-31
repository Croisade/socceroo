import pandas as pd
import os

directory = './data'

all_data = pd.DataFrame()
for filename in os.listdir(directory):
    if filename.endswith('.xls'):
        file_path = os.path.join(directory, filename)
        list_of_dfs = pd.read_html(file_path)
        for df in list_of_dfs:  # Iterate over each DataFrame in the list
            all_data = pd.concat([all_data, df], ignore_index=True)


all_data.to_excel('mls_combined.xlsx', index=False)