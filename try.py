import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("YouTube downloader")


# window window
window.geometry("400x500")
window.configure(bg="#272B2A")
window.resizable(0, 0)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=3)




# Create a label with text
label = tk.Label(window, text="Enter something:")
label.configure(bg="#333333" ,)
label.grid(row=0,column=3)


# creating the search bar 
entry = tk.Entry(window,width=40,bg='#6E6B62')
entry.grid(row=1,column=3)



























window.mainloop()
