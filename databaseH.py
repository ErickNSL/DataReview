import kagglehub
import pandas as pd
import re



#Dowload the dataset and import to the path
#path = kagglehub.dataset_download("shubhambathwal/flight-price-prediction")
#print(f'The path were the dataset was storaged is {path}')


#load the data into a df
economy_df = pd.read_csv('2/economy.csv')

# Check First Row
print(economy_df.head(1))

# Function to Fix 'time_taken' Format
def fix_time_taken(time_str):
    match = re.match(r'(\d{1,2})h (\d{1,2})m', time_str)  # Allow 1 or 2 digits for hours
    if match:
        hour = match.group(1).zfill(2)  # Ensure 2-digit hour
        minute = match.group(2).zfill(2)  # Ensure 2-digit minute
        return f"{hour}:{minute}"  # Format as hh:mm
    return time_str  # Return original if no match

# Apply Fix to 'time_taken'
economy_df['time_taken'] = economy_df['time_taken'].apply(fix_time_taken)

# Convert to timedelta
economy_df['time_taken'] = pd.to_timedelta(economy_df['time_taken'] + ':00')  # Append seconds for valid format

# Check Output
print(economy_df.head(1))

min_time = economy_df["time_taken"].min()
max_time = economy_df["time_taken"].max()
print(f"Min Time: {min_time}, Max Time: {max_time}")



# #Read the main information(structure, rows and columns(Shape))
# print('\nInconsistent values of economy and business [time_taken]')
# ecoinvalid_timetaken = economy_df['time_taken'].str.len() != 7
# print(f'economy {ecoinvalid_timetaken.sum()}')

# ### this shows the index with the inconsistencie
# inconsistent_indices = economy_df[ecoinvalid_timetaken].index
# print(ecoinvalid_timetaken.index)


# print(economy_df['time_taken'].unique(  ))
