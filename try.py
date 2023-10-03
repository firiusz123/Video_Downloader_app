import tkinter as tk
from tkinter import filedialog
import os

def search_for_video():
    entered_text = entry.get()
    label.config(text="You entered: " + entered_text)
    entry.delete(0,tk.END)
def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder_label.config(text=f"Selected Folder: {folder_path}")

def open():
    os.system("explorer C:\\ folder dir")



# Create the main window
window = tk.Tk()
window.title("YouTube downloader")
window.geometry("400x300")
window.configure(bg="#333333")
window.grid()

# Create a label with text
label = tk.Label(window, text="Enter something:")
label.configure(bg="#333333" ,)
label.grid(row=0,column=0)



# Create an entry widget
entry = tk.Entry(window)
entry.grid(row=0,column=1)

# Create a button to submit
submit_button = tk.Button(window, text="Search", command=search_for_video)
submit_button.grid(row=1,column=0)

label1 = tk.Button(window, text="Pre TC", fg="red", font=("Ariel", 9, "bold"), command=open)
label1.grid(row=1,column=2)

# Run the main loop
window.mainloop()





















window.mainloop()
