#Importation des modules

from tkinter.filedialog import askdirectory
from tkinter import*

root = Tk()
scrool = Scrollbar()
scrool.pack(side=RIGHT, fill=Y)

liste = Listbox(root, yscrollcommand = scrool.set)
for a in range(1, 100):
    liste.insert(END, "hello world" + str(a))
liste.pack(side=LEFT, fill=BOTH)

scrool.config(command=liste.yview)

root.mainloop()





