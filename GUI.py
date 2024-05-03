from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
import TerpHousingHub as logic

def click():
    logic.find_listing(entry_string.get())

#window
root = ttk.Window(themename = 'morph')
root.title('TerpHousingHub')
root.geometry('1000x900')

# title
title_label = ttk.Label(root, text = "Terp Housing Hub", font = 'Calibri 30')
title_label.pack(pady = 10)

# variables
entry_string = tk.StringVar()
rating = ttk.DoubleVar(value = 3.5)
new_rating = ttk.DoubleVar(value = 3.5)

#input field
input_frame = ttk.Frame(root, padding = 15)
input_lf = ttk.Labelframe(input_frame, text = "Search for a specific address to find reviews from past tennants or post a review yourself", padding = 15)
#Search field
search_field = ttk.Frame(input_lf)
entry_label = ttk.Label(search_field, text = "Address", width = 8)
entry_label.pack(side=LEFT, padx=(15, 0))
search_entry = ttk.Entry(search_field, textvariable = entry_string)
search_entry.pack(side ='left', fill=X, expand=YES, padx=5)
search_button = ttk.Button(search_field, text='Search', command = click, width = 8)
search_button.pack(side ='left', padx = 5)
search_field.pack(fill=X, expand=YES)
# Browse Options
browse_field = ttk.Frame(input_lf)
or_label = ttk.Label(browse_field, text = "OR", width = 5)
browse_label = ttk.Label(browse_field, text = "Browse for listings", width = 15)
or_label.pack()
browse_label.pack(side='left', padx=(15,0))

#Radio Buttons
campus = ttk.StringVar()
on_radio = ttk.Radiobutton(browse_field, text = "On Campus", value = "oncampus", variable = campus)
on_radio.pack(side=LEFT, padx = 5)
off_radio = ttk.Radiobutton(browse_field, text = "Off Campus", value = "offcampus", variable = campus)
off_radio.pack(side=LEFT, padx = 5)


#Rating Scale
rating_field = ttk.Frame(browse_field)
rating_label = ttk.Label(rating_field, text="Minimum Rating of:")
rating_label.pack(side=LEFT)
rating_value = ttk.Label(rating_field, textvariable=rating)
rating_value.pack(side=LEFT)
rating_scale = tk.Scale(rating_field, from_= 1, to = 5, variable = rating, orient=HORIZONTAL, tickinterval=1, sliderlength = 10, length = 300, resolution=.1, fg = "white")
rating_scale.pack(side=LEFT, padx=15)
rating_field.pack(fill=X, expand=YES, padx=20)
browse_button = ttk.Button(rating_field, text="Browse", width = 8)
browse_button.pack(side="right")
browse_field.pack(fill=X, expand=YES)
input_lf.pack(fill=X, anchor=N, expand=YES)
input_frame.pack(side="top", fill=BOTH, expand=YES)

#output field
output_frame = ttk.Frame(root)
output_string = ttk.StringVar()
output_label = ttk.Label(output_frame, text = 'Results', font = 'Calibri 15', textvariable = output_string)

# Treeview
tree = ttk.Treeview(output_frame)
tree['columns'] = ('address', 'rating', 'On campus', 'contact')

tree.column("#0", width=0, stretch=NO)
tree.column("address", anchor=W, width=300)
tree.column("rating", anchor=W, width=100)
tree.column("On campus", anchor=CENTER, width=100)
tree.column("contact", anchor=W, width=300)

tree.heading("#0", text='', anchor=W)
tree.heading("address", text='Address', anchor=W)
tree.heading("rating", text='Rating', anchor=W)
tree.heading("On campus", text='On Campus?', anchor=CENTER)
tree.heading("contact", text='Apply at:', anchor=W)

# Insert some data
count = 0
print(len(logic.housing))
for house in logic.housing:
    tree.insert(parent='', index='end', iid=count, text='', values= (house.address, house.avg_rating(), house.on_campus, house.apply))
    count += 1

tree.pack(fill=BOTH, expand=YES, pady=10, padx = 20)

#command field
command_frame = ttk.LabelFrame(output_frame, text ="Commands")
command_frame.pack(fill=X, expand=YES, padx=20)
command_scale = tk.Scale(command_frame, from_= 1, to = 5, variable = new_rating, orient=HORIZONTAL, tickinterval=1, sliderlength = 10, length = 300, resolution=.1, fg = "white")
command_scale.grid(row=0, column=0, padx=10, pady=10)
scale_label = ttk.Label(command_frame, textvariable=new_rating)
scale_label.grid(row=0, column=1, padx=10, pady=10)
rate_button = ttk.Button(command_frame, text = "Rate This Housing Unit")
rate_button.grid(row=0, column=2, padx=10, pady=10)
add_button = ttk.Button(command_frame, text = "Add New Housing Unit")
add_button.grid(row=1, column=0, padx=10, pady=10)

# Output label
output_string = ttk.StringVar()
output_label = ttk.Label(output_frame, text='Results', font='Calibri 15', textvariable=output_string)

# Pack the label after the Treeview
output_label.pack(pady=10)

# Pack the output frame into the root window
output_frame.pack(side="top", fill=BOTH, pady=10)

root.mainloop()