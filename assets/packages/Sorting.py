#coding utf-8
import os, os.path, shutil


class sorting:
    """
    sort file or directory to final directory
    """
    def __init__(self):
        """
        Intialisation variables 
        """
        self.final_directory = ''
        self.list_file = ''
        self.final_directory = ''
        self.path = { #liste des paths en fonction des lettres par lesquelles commencent le fichier
             'HG_' : 'C:/Users/cmaze/OneDrive/fichiers/école/3e/HG',
             'SPC_': 'C:/Users/cmaze/OneDrive/fichiers/école/3e/physique',
             "MATHS_": 'C:/Users/cmaze/OneDrive/fichiers/école/3e/maths'
            }
        self.file_path = ''
        

    def sort_directory_letters(self):
        try:
            self.start_directory = input("start folder: ")
        except OSError:
            print("dossier  introuvable")

        self.list_file = os.listdir(self.start_directory)
        for files in self.list_file:
            for k, v in self.path.items():
                if files.startswith(k):
                    self.file_path = os.path.join(self.start_directory, files)
                    shutil.move(self.file_path, self.path[k])
                    print("transfert effectué")
            



                    
            


