#coding utf-8
import os, os.path, shutil
from configparser import ConfigParser

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
        self.file_path = ''
        self.path_config = 'C:/Users/cmaze/OneDrive/developpement/python/projets systeme/File-sorter-and-security/configuration'
        self.parser = ConfigParser()
        self.content = None
        self.method_ext = None
        self.method_lett = None
        self.path_letters = None
        self.paths_ext = None
        self.pl = None

    def get_info_config_ini(self):
        os.chdir(self.path_config)
        self.parser.read('config.ini')
        self.method_ext = self.parser.get("method", "extension")
        self.method_lett = self.parser.get("method", "letters")
        
                

sort = sorting()
sort.get_info_config_ini()

        
            


sorter = sorting()
sorter.get_info_config_ini()




            
        
        



            



                    
            


