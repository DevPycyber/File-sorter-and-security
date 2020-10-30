import tkinter
from tkinter import filedialog
import json
from assets.packages.Sorting import sorting
from tkinter import BooleanVar




class Interface:
    def __init__(self, hight, larg, title):
        self.main_windows = tkinter.Tk()
        self.main_windows.title(title)
        self.main_windows.geometry("{}x{}".format(larg, hight))
        
        #check buttons variables
        self.check_extension = tkinter.BooleanVar()
        self.check_letters = tkinter.BooleanVar()

        #Label
        self.presentation = tkinter.Label(self.main_windows, text="Configuration des paramètres de tri", font=("Courrier", 15))
        self.button_check_extension = tkinter.Checkbutton(self.main_windows, text="trier grâce aux extensions des fichiers",
                font=("Arial", 20), variable=self.check_extension)

        self.button_check_letters = tkinter.Checkbutton(self.main_windows, text="trier grâce aux lettres composant le nom du fichier",
        font=("Arial", 20), variable=self.check_letters)
        self.paths_extensions = tkinter.Text(self.main_windows, height=5, state="disabled")
        self.paths_letters = tkinter.Text(self.main_windows, height=5, state="disabled") 
        self.browse_button = tkinter.Button(self.main_windows, text="browse", font=("Arial", 15), state="disabled")

    def place_widgets(self):
        self.browse_button.place(x=700, y=150)
        self.paths_extensions.place(x=200, y=300)
        self.button_check_extension.place(x=200, y=150)
        self.button_check_letters.place(x=200, y=250)
        self.presentation.pack(anchor='n')
        self.browse_button.place()
    
    #fonctions check buttons

    def change_app_ext(self):
        if self.paths_extensions.cget("state") == 'normal':
            self.paths_extensions.config(state='disabled')
        else:
            self.paths_extensions.config(state='normal')

    def change_app_lett(self):
        if self.paths_letters.cget("state") == 'normal':
            self.paths_letters.config(state='disabled')
        else:
            self.paths_letters.config(state='normal')

    def browse_directory(self):
        self.directory_name = filedialog.askdirectory(initialdir = "/",
                                            title="Select a folder")
        return self.directory_name
            

        