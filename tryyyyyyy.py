import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_text.set(listbox.get(selected_index))

# Create a Tkinter window
window = tk.Tk()
window.title("List with Scrollbar Glued")

# Create a button above the list
button_above = tk.Button(window, text="Button Above")
button_above.pack()

# Create a frame to contain the Listbox and Scrollbar
list_frame = tk.Frame(window)
list_frame.pack()

# Create a Listbox widget for the list
listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=10)
for item in range(1, 21):
    listbox.insert(tk.END, f"Item {item}")
listbox.pack(side=tk.LEFT)

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Connect the Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a button below the list
button_below = tk.Button(window, text="Button Below")
button_below.pack()

# Create a label to display the selected item
selected_text = tk.StringVar()
selected_label = tk.Label(window, textvariable=selected_text)
selected_label.pack()

# Bind the Listbox selection event to a function
listbox.bind("<<ListboxSelect>>", on_select)

window.mainloop()
