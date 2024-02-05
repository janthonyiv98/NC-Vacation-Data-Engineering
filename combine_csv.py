import pandas as pd
import os

# Code inspired by: https://raredogmarketing.com/resources/combining-multiple-csv-files-into-one-file-using-python-step-by-step-guide
# create path to csv files in 2023 Weather Data folder
project_folder = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(project_folder, '2023_Weather_Data')

all_files = os.listdir(folder_path)

# Filter out non-CSV files
csv_files = [f for f in all_files if f.endswith('.csv')]

# Create a list to hold the dataframes
df_list = []

for csv in csv_files:
    file_path = os.path.join(folder_path, csv)
    try:
        # Try reading the file using default UTF-8 encoding
        df = pd.read_csv(file_path)
        df_list.append(df)
           
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
            df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
            df_list.append(df)
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    except Exception as e:
        print(f"Could not read file {csv} because of error: {e}")

# concatenate all data into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# create a new index
combined_df["id"] = combined_df.index + 1

# create a dictionary for city names to NC_ID
city_mapping = {
    'Asheville': 'nc01',
    'Banner Elk': 'nc02',
    'Boone': 'nc03',
    'Charlotte': 'nc04',
    'Cherokee': 'nc05',
    'Emerald Isle': 'nc06',
    'High Point': 'nc07',
    'Nags Head': 'nc08',
    'Ocracoke': 'nc09',
    'Raleigh': 'nc10',
    'Wilmington': 'nc11',
    'Winston-Salem': 'nc12'
}

# iterate through the cities and update the 'NC_ID' column
for city, nc_id in city_mapping.items():
    combined_df.loc[combined_df['name'].str.contains(city, case=False, na=False), 'NC_ID'] = nc_id

# Move columns to front
first_column = combined_df.pop('id')
second_column = combined_df.pop('NC_ID')

combined_df.insert(0, 'id', first_column)
combined_df.insert(1, 'NC_ID', second_column)

# Save the final result to a new CSV file
combined_df.to_csv('combined_data.csv',encoding='utf-8', index=False)