import pandas as pd
import os

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

# Concatenate all data into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# create a new index
combined_df["id"] = combined_df.index + 1

 # add identifier numbers
combined_df.loc[combined_df['name'].str.contains('Asheville', case=False, na=False), 'NC_ID'] = 'nc01'
combined_df.loc[combined_df['name'].str.contains('Banner Elk', case=False, na=False), 'NC_ID'] = 'nc02'
combined_df.loc[combined_df['name'].str.contains('Boone', case=False, na=False), 'NC_ID'] = 'nc03'
combined_df.loc[combined_df['name'].str.contains('Charlotte', case=False, na=False), 'NC_ID'] = 'nc04'
combined_df.loc[combined_df['name'].str.contains('Cherokee', case=False, na=False), 'NC_ID'] = 'nc05'
combined_df.loc[combined_df['name'].str.contains('Emerald Isle', case=False, na=False), 'NC_ID'] = 'nc06'
combined_df.loc[combined_df['name'].str.contains('High Point', case=False, na=False), 'NC_ID'] = 'nc07'
combined_df.loc[combined_df['name'].str.contains('Nags Head', case=False, na=False), 'NC_ID'] = 'nc08'
combined_df.loc[combined_df['name'].str.contains('Ocracoke', case=False, na=False), 'NC_ID'] = 'nc09'
combined_df.loc[combined_df['name'].str.contains('raleigh', case=False, na=False), 'NC_ID'] = 'nc10'
combined_df.loc[combined_df['name'].str.contains('Wilmington', case=False, na=False), 'NC_ID'] = 'nc11'
combined_df.loc[combined_df['name'].str.contains('Winston-Salem', case=False, na=False), 'NC_ID'] = 'nc12'

# Move columns to front
first_column = combined_df.pop('id')
second_column = combined_df.pop('NC_ID')

combined_df.insert(0, 'id', first_column)
combined_df.insert(1, 'NC_ID', second_column)

# Save the final result to a new CSV file
combined_df.to_csv('combined_data.csv',encoding='utf-8', index=False)