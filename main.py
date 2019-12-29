import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Wikipedia")
root.geometry('220x60')


def search(event=None):
    search = entry.get()
    answer = wikipedia.summary(search)
    showinfo("Wikipedia Answer", answer)


# Label
label = Label(root, text="Wikipedia Search :")
label.grid(row=0, column=0)

# Search Box
entry = Entry(root)
entry.grid(row=1, column=0, padx=(10, 0))

# Search button
button = Button(root, text="Search", command=search)
button.grid(row=1, column=1, padx=10)


button.bind('<Enter>', func=search)
root.mainloop()
