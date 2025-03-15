import kagglehub
import pandas as pd
import re



#Dowload the dataset and import to the path
#path = kagglehub.dataset_download("shubhambathwal/flight-price-prediction")
#print(f'The path were the dataset was storaged is {path}')


#load the data into a df
busniness = pd.read_csv('2/business.csv')
economy_df = pd.read_csv('2/economy.csv')

# Check First Row
print(busniness.groupby('airline').size().sort_values(ascending=True))





# #Read the main information(structure, rows and columns(Shape))
# print('\nInconsistent values of economy and business [time_taken]')
# ecoinvalid_timetaken = economy_df['time_taken'].str.len() != 7
# print(f'economy {ecoinvalid_timetaken.sum()}')

# ### this shows the index with the inconsistencie
# inconsistent_indices = economy_df[ecoinvalid_timetaken].index
# print(ecoinvalid_timetaken.index)


# print(economy_df['time_taken'].unique(  ))
