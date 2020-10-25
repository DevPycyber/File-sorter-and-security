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
        self.choice = ''
        self.final_directory = ''
        self.list_file = ''
        self.final_directory = ''
        self.path_letter = { #liste des paths en fonction des lettres par lesquelles commencent le fichier
             'HG_' : 'C:/Users/cmaze/OneDrive/fichiers/école/3e/HG',
             'SPC_': 'C:/Users/cmaze/OneDrive/fichiers/école/3e/physique',
             "MATHS_": 'C:/Users/cmaze/OneDrive/fichiers/école/3e/maths'
            }
        self.path_extension = { #liste des paths en fonction de l'extension du fichier
                '.docx': "C:/Users/cmaze/Onedrive/Public/Public/Documents",
                '.txt': "C:/Users/cmaze/Onedrive/Public/Public/Documents",
                '.pdf': "C:/Users/cmaze/Onedrive/Public/Public/Documents"    
            }
            
        self.file_path = ''
        

    def choice_sort(self):
        try:
            self.file_path = input("start folder? ")
            assert os.path.isdir(self.file_path)
            
        except AssertionError:
            print("Folder not found, please retry: ")
            self.file_path = input("start folder? ")
        
        self.choice = input("letters or extensions?(l, e) ")
        self.list_file = os.listdir(self.file_path)
        
        
        for files in self.list_file:
            if self.choice == 'l':           
                for k, v in self.path_letter.items():
                    if files.startswith(k):
                        self.final_directory = self.path_letter[k]
                        self.start_directory = os.path.join(self.file_path, files)
                        shutil.move(self.start_directory, self.final_directory)
                        
            elif self.choice == 'e':
                for k1, v1 in self.path_extension.items():
                    if files.endswith(k1):
                        self.final_directory = self.path_extension[k1]
                        self.start_directory = os.path.join(self.file_path, files)
                        shutil.move(self.start_directory, self.final_directory)
        print("transfert effectué")

                
        
            



            



                    
            


