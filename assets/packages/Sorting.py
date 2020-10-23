#coding utf-8
import os
import os.path
import shutil
from getpass import getuser

class sorting:
    """
    sort file or directory to final directory
    """
    def __init__(self):
        """
        Intialisation variables 
        """
        self.courant_path = ''
        self.extension = ''
        self.final_directory = ''
        self.list_file = ''
        self.file_name = ''
        self.final_directory = ''
        self.user_name = ''
        

    def determine_path(self, final_directory):
        self.user_name = getuser()
        self.directory = os.path.join("C:/Users", self.user_name, final_directory)

    def sort_directory(self, courant_path, extension):
        self.courant_path = sorting.determine_path(self.courant_path)
        os.chdir(self.courant_path)
        self.final_directory = sorting.determine_path(self.final_directory)
        if not os.path.exists(self.final_directory):
            print("regive your final path: ")
        
        
        else:
            for files in self.list_file:
                self.file_name = os.path.splitext(files)
                if self.file_name[1] == self.extension:
                    shutil.move(files, self.final_directory)

                    
            
sorting = sorting()
sorting.sort_directory('Documents', 'Images')

