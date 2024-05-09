"""
This script contains all of the user interface and methods for updating that
user interface. Methods that change what the user sees are placed in this script.
"""
import tkinter as tk
import ttkbootstrap as ttk
import TerpHousingHub as logic

# Functions for connecting the logic from TerpHousingHub to the User Interface
def refresh_data():
    """This method adds the data from the housing list to a treeview we are 
    using to display results. It is also used to reset the treeview to perform 
    new searches.
    """
    for item in tree.get_children():
        tree.delete(item)
    count = 0
    for house in logic.housing:
        root = tree.insert(parent='', 
                            index='end', 
                            iid=count, 
                            text='', 
                            values= (house.address, house.avg_rating(),
                                    house.on_campus, house.apply))
        for review in house.reviews:
            tree.insert(root, 'end', text=review, values=(review,))
        count += 1
    
def search_listing():
    """Takes user's search request and looks for it in the addresses of the
    properties in the treeview. This updates the treeview to only properties 
    that contain the search request in it's address.
    """
    refresh_data()
    prop = entry_string.get().upper()
    for item in tree.get_children():
        if prop not in tree.item(item, "values")[0]:
            tree.delete(item)

def browse_listings():
    """Makes it so the treeview only contains properties that match the
    browsing criteria.
    """
    refresh_data()
    for item in tree.get_children():
        if (float(tree.item(item, "values")[1]) < rating.get() 
            or tree.item(item, "values")[2] != str(campus.get())):
                tree.delete(item)

def new_listing():
    """Takes user input and calls the add_listing function to create a new 
    property and add it to the list containing all the housing units
    """
    logic.add_listing(add_string.get(), add_campus.get(), contact_var.get())
    refresh_data()

def rate():
    """Adds a rating using add_rating method to add number rating and string 
    comments to selected property on treeview.
    """
    selected = tree.focus()
    address = tree.item(selected, 'values')[0]
    property_obj = logic.find_listing(address)
    property_obj.add_rating(new_rating.get(), new_review.get())
    refresh_data()

#window
root = ttk.Window(themename = 'morph')
root.title('TerpHousingHub')
root.geometry('1200x650')

# title
title_label = ttk.Label(root, text = "Terp Housing Hub", font = 'Calibri 30')
title_label.pack(pady = 10)

# variables
entry_string = tk.StringVar()
add_string = tk.StringVar()
rating = ttk.DoubleVar(value = 3.5)
campus = ttk.BooleanVar()
new_rating = ttk.DoubleVar()
new_review = ttk.StringVar()
add_campus = ttk.BooleanVar()
contact_var = ttk.StringVar()

#input field
input_frame = ttk.Frame(root, padding = 15)
input_lf = ttk.Labelframe(input_frame, 
        text = "Search for a specific address to find reviews from past\
        tennants or post a review yourself", 
        padding = 15)
#Search field
search_field = ttk.Frame(input_lf)
entry_label = ttk.Label(search_field, text = "Address", width = 8)
entry_label.pack(side='left', padx=(15, 0))
search_entry = ttk.Entry(search_field, textvariable = entry_string)
search_entry.pack(side ='left', fill='x', expand='yes', padx=5)
search_button = ttk.Button(search_field, text='Search', 
                command = search_listing, width = 8)
search_button.pack(side ='left', padx = 5)
search_field.pack(fill='x', expand='yes')
# Browse Options
browse_field = ttk.Frame(input_lf)
or_label = ttk.Label(browse_field, text = "OR", width = 5)
browse_label = ttk.Label(browse_field, text = "Browse for listings", 
                width = 15)
or_label.pack()
browse_label.pack(side='left', padx=(15,0))

#Radio Buttons
on_radio = ttk.Radiobutton(browse_field, text = "On Campus", value = True, 
            variable = campus)
on_radio.pack(side='left', padx = 5)
off_radio = ttk.Radiobutton(browse_field, text = "Off Campus", value = False, 
            variable = campus)
off_radio.pack(side='left', padx = 5)


#Rating Scale
rating_field = ttk.Frame(browse_field)
rating_label = ttk.Label(rating_field, text="Minimum Rating of:")
rating_label.pack(side='left')
rating_value = ttk.Label(rating_field, textvariable=rating)
rating_value.pack(side='left')
rating_scale = tk.Scale(rating_field, 
                        from_= 1, 
                        to = 5, 
                        variable = rating, 
                        orient="horizontal", 
                        tickinterval=1, 
                        sliderlength = 10, 
                        length = 300, 
                        resolution=.1, 
                        fg = "white")
rating_scale.pack(side='left', padx=15)
rating_field.pack(fill='x', expand='yes', padx=20)
browse_button = ttk.Button(rating_field, text="Browse", 
                        width = 8, command = browse_listings)
browse_button.pack(side="right")
browse_field.pack(fill='x', expand='yes')
input_lf.pack(fill='x', anchor='n', expand='yes')
input_frame.pack(side="top", fill='both', expand='yes')

#output field
output_frame = ttk.Frame(root)
output_string = ttk.StringVar()
output_label = ttk.Label(output_frame, text = 'Results', 
                font = 'Calibri 15', textvariable = output_string)

# Treeview
tree = ttk.Treeview(output_frame)
tree['columns'] = ('address', 'rating', 'On campus', 'contact')

tree.column("#0", width=0, stretch="no")
tree.column("address", anchor='w', width=300)
tree.column("rating", anchor='w', width=100)
tree.column("On campus", anchor='center', width=100)
tree.column("contact", anchor='w', width=300)

tree.heading("#0", text='', anchor='w')
tree.heading("address", text='Address', anchor='w')
tree.heading("rating", text='Rating', anchor='w')
tree.heading("On campus", text='On Campus?', anchor='center')
tree.heading("contact", text='Apply at:', anchor='w')

# Insert some data
refresh_data()
tree.pack(fill='both', expand='yes', pady=10, padx = 20)

#command field
command_frame = ttk.LabelFrame(output_frame, text ="Commands")
command_frame.pack(fill='x', expand='yes', padx=20)
review_label = ttk.Label(command_frame, text="Leave a comment:")
review_label.grid(row=0, column=0, padx=10, pady=10)
review_entry = ttk.Entry(command_frame, textvariable = new_review)
review_entry.grid(row=0, column=1, padx=10, pady=10)
rate_entry = ttk.Entry(command_frame, width=10, textvariable = new_rating)
rate_entry.grid(row=0, column=2, padx=10, pady=10)
rate_button = ttk.Button(command_frame, text = "Rate This Housing Unit", 
                        command = rate)
rate_button.grid(row=0, column=3, padx=10, pady=10)
add_label = ttk.Label(command_frame, text = "Address:", width = 8)
add_label.grid(row=1, column=0, padx=0, pady=10)
add_entry = ttk.Entry(command_frame, textvariable = add_string)
add_entry.grid(row=1, column=1, padx=10, pady=10)
contact_label = ttk.Label(command_frame, text = "Info at:", width = 8)
contact_label.grid(row=1, column=2, padx=0, pady=10)
contact_entry = ttk.Entry(command_frame, textvariable = contact_var, width=20)
contact_entry.grid(row=1, column=3, padx=0, pady=10)
add_on = ttk.Radiobutton(command_frame, text = "On Campus", value = True, 
                        variable = add_campus)
add_on.grid(row=1, column=4, padx=10, pady=10)
add_off = ttk.Radiobutton(command_frame, text = "Off Campus", value = False, 
                        variable = add_campus)
add_off.grid(row=1, column=5, padx=10, pady=10)
add_button = ttk.Button(command_frame, text = "Add New Housing Unit", 
                        command=new_listing)
add_button.grid(row=1, column=6, padx=20, pady=10)

# Output label
output_string = ttk.StringVar()
output_label = ttk.Label(output_frame, text='Results', font='Calibri 15', 
                        textvariable=output_string)

# Pack the label after the Treeview
output_label.pack(pady=10)

# Pack the output frame into the root window
output_frame.pack(side="top", fill='both', pady=10)

root.mainloop()