import tkinter as tk
from tkinter import messagebox, simpledialog

win = tk.Tk()
win.title("Recipe Book App")

# Lists to store recipe names, ingredients, and instructions
recipe_names_list = []
recipe_ingredients_list = []
recipe_instructions_list = []

# Function to add a recipe
def add_recipe():
    recipe_name = simpledialog.askstring("Add Recipe", "Enter recipe name:")

    if not recipe_name:
        messagebox.showwarning("Input Error", "Recipe name is required.")
        return

    if recipe_name in recipe_names_list:
        messagebox.showwarning("Duplicate Recipe", "This recipe already exists.")
        return

    ingredients = simpledialog.askstring("Add Recipe", "Enter ingredients (separated by commas):")
    instructions = simpledialog.askstring("Add Recipe", "Enter cooking instructions:")

    if ingredients and instructions: # have value
        recipe_names_list.append(recipe_name)  # Add to recipe names list
        recipe_ingredients_list.append(ingredients)  # Add ingredients
        recipe_instructions_list.append(instructions)  # Add instructions
        recipe_listbox.insert(tk.END, recipe_name)  # Add to listbox, appear at the end of the list
        messagebox.showinfo("Success", f"Recipe '{recipe_name}' added successfully.")
    else:
        messagebox.showwarning("Input Error", "Ingredients and instructions are required.")

# Function to view the selected recipe's details
def view_recipe(event): # parameter, becuz the function is bound to a Listbox selection event
    selection = recipe_listbox.curselection() # tuple method
    if not selection:
        return

    index = selection[0] # if the first recipe is selected, selection will be (0,) index will be 0, 
    recipe_details_text.delete(1.0, tk.END) # 1.0 means line 1, character 0
    recipe_details_text.insert(tk.END, f"Recipe: {recipe_names_list[index]}\n")
    recipe_details_text.insert(tk.END, f"Ingredients: {recipe_ingredients_list[index]}\n\n")
    recipe_details_text.insert(tk.END, f"Instructions: {recipe_instructions_list[index]}")

# Function to edit an existing recipe
def edit_recipe():
    selection = recipe_listbox.curselection()
    if not selection: 
        messagebox.showwarning("Selection Error", "Please select a recipe to edit.")
        return

    index = selection[0] # position of recipe in recipe_names_list
    new_ingredients = simpledialog.askstring("Edit Recipe", "Edit ingredients:", initialvalue=recipe_ingredients_list[index]) # initial value means set the initial value in the input box to the current ingredients of the selected recipe
    new_instructions = simpledialog.askstring("Edit Recipe", "Edit instructions:", initialvalue=recipe_instructions_list[index])

    if new_ingredients and new_instructions: # Checks if both new values are provided
        recipe_ingredients_list[index] = new_ingredients
        recipe_instructions_list[index] = new_instructions
        messagebox.showinfo("Success", f"Recipe '{recipe_names_list[index]}' updated successfully.")
        view_recipe(None)  # to view recipe details by calling the function without passing an event, none is pass bcuz view_recipe is trigger by an event

# Function to delete the selected recipe
def delete_recipe():
    selection = recipe_listbox.curselection()
    if not selection:
        messagebox.showwarning("Selection Error", "Please select a recipe to delete.")
        return

    index = selection[0]
    recipe_name = recipe_names_list[index]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{recipe_name}'?")
    if confirm:
        del recipe_names_list[index] # delete item from list
        del recipe_ingredients_list[index]
        del recipe_instructions_list[index]
        recipe_listbox.delete(index) # delete selected item from listbox
        recipe_details_text.delete(1.0, tk.END)  # Clear details box
        messagebox.showinfo("Deleted", f"Recipe '{recipe_name}' deleted.")

# Function to search recipes
def search_recipe():
    search_term = simpledialog.askstring("Search Recipe", "Enter recipe name:")
    
    if not search_term:
        messagebox.showwarning("Input Error", "Please enter a recipe name.")
        return
    
    if search_term in recipe_names_list:
        index = recipe_names_list.index(search_term)
        recipe_details_text.delete(1.0, tk.END)  # Clear the text box
        recipe_details_text.insert(tk.END, f"Recipe: {recipe_names_list[index]}\n")
        recipe_details_text.insert(tk.END, f"Ingredients: {recipe_ingredients_list[index]}\n\n")
        recipe_details_text.insert(tk.END, f"Instructions: {recipe_instructions_list[index]}")
        recipe_listbox.selection_clear(0, tk.END)  # Clear previous selection
        recipe_listbox.selection_set(index)  # Highlight the searched recipe
    else:
        messagebox.showinfo("Not Found", f"Recipe '{search_term}' not found.")
        



# Recipe Listbox (displays list of recipe names)
recipe_listbox = tk.Listbox(win, height=10, width=40, bg="sky blue")
recipe_listbox.grid(row=0, column=0, columnspan=3, pady=10)

# Bind select event to view_recipe
recipe_listbox.bind('<<ListboxSelect>>', view_recipe)

# Buttons for adding, editing, and deleting recipes
add_button = tk.Button(win, text="Add Recipe", command=add_recipe, bg="yellow")
add_button.grid(row=1, column=0)

edit_button = tk.Button(win, text="Edit Recipe", command=edit_recipe, bg="orange")
edit_button.grid(row=1, column=1)

delete_button = tk.Button(win, text="Delete Recipe", command=delete_recipe, bg="red")
delete_button.grid(row=1, column=2)

search_button = tk.Button(win, text="Search Recipe", command=search_recipe, bg="light green")
search_button.grid(row=2, column=1, pady=10)

# Quit button to exit the app
quit_button = tk.Button(win, text="Quit", command=win.quit, bg="light gray")
quit_button.grid(row=4, column=1, pady=10)

# Text box for displaying recipe details
recipe_details_text = tk.Text(win, width=40, height=10, wrap=tk.WORD, bg="light pink")
recipe_details_text.grid(row=3, column=0, columnspan=3, pady=10)


win.mainloop()