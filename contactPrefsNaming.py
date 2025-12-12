import pandas as pd
from datetime import datetime  
import os
import tkinter as tk
from tkinter import dnd
from tkinterdnd2 import DND_FILES, TkinterDnD

# Get the current date
current_date = datetime.now()

# Extract day, month, and year
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year


# Drag and drop GUI

root = TkinterDnD.Tk()
root.title("Drop CSV File")
root.geometry("300x150")

data = None

def drop(event):
    global data
    file_path = event.data.strip('{}')
    
    if file_path and file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
        label.config(text=f"Loaded: {file_path.split('/')[-1]}")
        root.destroy()
    else:
        label.config(text="Please drop a CSV file")

label = tk.Label(root, text="Drop CSV file here. Instructions are in the Box folder.", pady=50)
label.pack()

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)
root.mainloop()

# converting column data to list
names = data['USER NAME'].tolist()

# filter names
def filter_names(names):
    # Remove duplicates and handle non-string values
    return list(set(str(name) for name in names if pd.notna(name)))

def firstName(filtered_names):
    first_names = []
    for name in filtered_names:
        parts = name.split(' ')
        # If there's a middle name/initial, include it with the first name
        if len(parts) > 2:
            first_names.append(' '.join(parts[:-1]))
        else:
            first_names.append(parts[0])
    return first_names

def lastName(filtered_names):
    last_names = [name.split(' ')[-1] for name in filtered_names]
    return last_names

def fileNames(names):
    filtered_names = filter_names(names)
    first = firstName(filtered_names)
    last = lastName(filtered_names)
    nameList = [f"{current_year}.{current_month}.{current_day} {last[i]}, {first[i]} Unsubscribe AB" for i in range(len(filtered_names))]
    nameList.sort()
    return '\n'.join(nameList)

def createFile(names):
    filename = f"{current_month}_{current_day}_{current_year}_contactPrefs.txt"
    with open(filename, "w") as f:
        f.write(fileNames(names))

    abs_path = os.path.abspath(filename)

    # Show output in a simple GUI window
    output_window = tk.Tk()
    output_window.title("File Created")
    output_window.geometry("500x300")

    with open(filename, "r") as f:
        content = f.read()

    text_widget = tk.Text(output_window, wrap="word")
    text_widget.insert("1.0", content)
    text_widget.config(state="disabled")
    text_widget.pack(expand=True, fill="both")

    label = tk.Label(output_window, text=f"File saved at:\n{abs_path}", pady=10)
    label.pack()

    output_window.mainloop()

createFile(names)
