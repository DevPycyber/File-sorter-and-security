#importation des différents modules
from tkinter import *


#affichage de la fenêtre
windows = Tk()
windows.geometry("800x600")

Entry1 = Text(windows, width=30, font=("Arial, 10"))


scroll = Scrollbar(windows)
Entry1.configure(yscrollcommand=scroll.set)

scroll.config(command=Entry1.yview)
Entry1.pack(fill=Y)

windows.mainloop()