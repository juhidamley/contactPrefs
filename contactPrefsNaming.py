# importing module
import pandas as pd

from datetime import datetime  # Import datetime module

import os

# Get the current date
current_date = datetime.now()

# Extract day, month, and year
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year


# reading CSV file
data = pd.read_csv(r"C:\Users\jdamley28\Downloads\contactPrefs.csv")

# converting column data to list
names = data['USER NAME'].tolist()

# filter names
def filter_names(names):
    # Remove duplicates and handle non-string values
    return list(set(str(name) for name in names if pd.notna(name)))

def firstName(names):
    filtered_names = filter_names(names)
    first_names = [name.split(' ')[0] for name in filtered_names]  # Split by space and take the first part
    return first_names

def lastName(names):
    filtered_names = filter_names(names)
    last_names = [name.split(' ')[-1] for name in filtered_names]  # Split by space and take the last part
    return last_names

def fileNames(names):
    filtered_names = filter_names(names)
    first = firstName(names)
    last = lastName(names)
    output = ""
    for i in range(len(filtered_names)):
        output += f"{current_year}.{current_month}.{current_day} {last[i]}, {first[i]} Unsubscribe AB\n"
    return output

def createFile(names):
    filename = f"{current_month}_{current_day}_{current_year}_contactPrefs.txt"
    f = open(filename, "w")
    f.write(fileNames(names))
    f.close()

    f = open(filename, "r")
    print(f.read())
    # absolute_path = f"C:/Users/jdamley28/Downloads/{filename}"
    abs_path = os.path.abspath(filename)
    print(abs_path)



print(fileNames(names))
#createFile(names)