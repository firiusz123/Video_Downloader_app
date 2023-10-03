import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
# Create a Tkinter window
window = tk.Tk()
window.title("YouTube downloader")


def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_text.set(listbox.get(selected_index))

def search_for_video():
    entered_text = entry.get()
    try:
        yt = YouTube(entered_text)
        label.config(text="The video title: " + yt.title)
    except:
        label.config(text="wrong link, try again :(")

def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        label2.configure(text=folder_path)









# window window
window.geometry("400x500")
window.configure(bg="#272B2A")
window.resizable(0, 0)







# Create a label with text
label = tk.Label(window, text="Enter YouTube link:" , fg='#ACAFC2')
label.configure(bg="#272B2A" ,height=1 )
label.pack()
# creating the search bar 
entry = tk.Entry(window,width=40,bg='#6E6B62')
entry.pack()
#creating a search  button 
button = tk.Button(window, bg='#6E6B62' , text='search for ',fg='black',command=search_for_video)
button.pack(pady = 10)





# Create a Listbox widget for the list
list_frame = tk.Frame(window,bg='#272B2A')

list_frame.pack()

label_choose = tk.Label(list_frame, text="Pick Video Resolution" , fg='#ACAFC2')
label_choose.configure(bg="#272B2A" ,height=1 )
label_choose.pack(side=tk.TOP, pady=20)

# Create a Listbox widget for the list
listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=8 ,bg='#6E6B62')
for item in range(1, 20):
    listbox.insert(tk.END, f"Item {item}")
listbox.pack(side=tk.LEFT)

# making a download button
download_button=tk.Button(list_frame, bg='#6E6B62' , text='Download the resolution ',fg='black')
download_button.pack(side=tk.RIGHT,padx=50)



# Create a vertical scrollbar
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL,highlightbackground='#6E6B62',background='#6E6B62')
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)






# Connect the Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#creating empty label for a spacing 
empty_label = tk.Label(window,height=4,bg="#272B2A")
empty_label.pack()





#a label  that shows a text 
label1 = tk.Label(window, text="The download folder is:" , fg='#ACAFC2')
label1.configure(bg="#272B2A" ,height=1 )
label1.pack()
# a label that should print out the current directory 
label2 = tk.Label(window, text="NONE" , fg='#ACAFC2')
label2.configure(bg="#272B2A" ,height=1 )
label2.pack()

folder_button=tk.Button(window, bg='#6E6B62' , text='Change Folder ',fg='black',command=open_folder_dialog)
folder_button.pack()






window.mainloop()
