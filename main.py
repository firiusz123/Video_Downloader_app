import tkinter as tk
import os

def search_for_video():
    entered_text = entry.get()
    label.config(text="You entered: " + entered_text)
    entry.delete(-1)
def open():
    os.system("explorer C:\\ folder dir")



# Create the main window
window = tk.Tk()
window.title("YouTube downloader")
window.geometry("400x300")
window.configure(bg="#333333")

# Create a label
label = tk.Label(window, text="Enter something:")
label.configure(bg="#333333" ,)
label.pack(pady=60 )



# Create an entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to submit
submit_button = tk.Button(window, text="Search", command=search_for_video)
submit_button.pack(pady=30)

label1 = tk.Button(window, text="Pre TC", fg="red", font=("Ariel", 9, "bold"), command=open)
label1.pack()

# Run the main loop
window.mainloop()
