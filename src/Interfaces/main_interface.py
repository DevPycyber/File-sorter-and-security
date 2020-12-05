import tkinter
from tkinter import filedialog
import json

from tkinter import BooleanVar


class Main_interface:
    def __init__(self, hight, larg, title):
        self.main_windows = tkinter.Tk()
        self.main_windows.title(title)
        self.main_windows.geometry("{}x{}".format(larg, hight))
        
        #variables
        self.listè_path_ext = []
        self.liste_path_lett = []

        #check buttons variables
        self.check_extension = tkinter.BooleanVar()
        self.check_letters = tkinter.BooleanVar()

        #Label

        self.presentation = tkinter.Label(self.main_windows, text="Configuration des paramètres de tri", font=("Courrier", 15))
        self.button_check_extension = tkinter.Checkbutton(self.main_windows, text="trier grâce aux extensions des fichiers",
                font=("Arial", 20), variable=self.check_extension)

        self.button_check_letters = tkinter.Checkbutton(self.main_windows, text="trier grâce aux lettres composant le nom du fichier",
        font=("Arial", 20), variable=self.check_letters)
        self.paths_extensions = tkinter.Entry(self.main_windows, state="normal")
        self.paths_letters = tkinter.Entry(self.main_windows, state="normal") 
        self.browse_button = tkinter.Button(self.main_windows, text="select a folder", font=("Cambria", 15), state="normal")
        self.valide_button = tkinter.Button(self.main_windows, text="valider", font=("Cambria", 15))
        self.select_extension = tkinter.Button(self.main_windows ,text="selectionner une extension", font=("Cambria", 17))

    def place_widgets(self):
        self.browse_button.place(x=700, y=150)
        self.paths_extensions.place(x=200, y=300)
        self.button_check_extension.place(x=200, y=150)
        self.button_check_letters.place(x=200, y=250)
        self.presentation.pack(anchor='n')
        self.select_extension.place(x=700, y=200)
        self.browse_button.place()
        
    
    #fonctions check buttons

    def browse_directory(self):
        self.directory_name = filedialog.askdirectory(title="select a folder")
        print(self.directory_name)

    def config_buttons(self):
        self.browse_button.config(command= lambda: Main_interface.browse_directory(self))

a = Main_interface(700, 1000, "first")
a.place_widgets()
a.config_buttons()
a.main_windows.mainloop()








        