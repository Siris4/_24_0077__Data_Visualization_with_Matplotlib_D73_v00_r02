import pandas as pd
import os

# figures out how many months of data was found in this dataset:

# Change the working directory
os.chdir('C:\\Users\\Siris\\Desktop\\GitHub Projects 100 Days NewB\\_24_0077__Day73_Data_Visualization_with_Matplotlib__240812\\NewProject\\r00-r09 START\\r00_env_START')

# Load the CSV file into a DataFrame
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# # Group by 'TAG' and sum the 'POSTS', then sort by the summed 'POSTS' in ascending order
# tag_totals_sorted = df.groupby('TAG')['POSTS'].sum().sort_values()
#
# # Print the sorted totals
# print(tag_totals_sorted)

# Convert the DATE column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Extract the month and year from the DATE column
df['MONTH'] = df['DATE'].dt.to_period('M')

# Group by the 'TAG' and 'MONTH' columns and sum the POSTS
monthly_post_counts = df.groupby(['TAG', 'MONTH']).agg({'POSTS': 'sum'})

# Count the number of unique months for each programming language (TAG)
monthly_count = monthly_post_counts.groupby('TAG').size().reset_index(name='MONTH_COUNT')

# Sort the programming languages by the number of months (ascending)
sorted_monthly_count = monthly_count.sort_values(by='MONTH_COUNT')

# Display the result
print(sorted_monthly_count)

