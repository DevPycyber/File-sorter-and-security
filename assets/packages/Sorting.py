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
        self.method_ext = ''
        self.method_lett = ''
        self.list_path_lett = {}
        self.list_path_ext = {}

        self.list_file = []


    def get_info_config_ini(self):
        os.chdir(self.path_config)
        self.parser.read('config.ini')
        self.method_ext = self.parser.get("method", "extension")
        self.method_lett = self.parser.get("method", "letters")
        if self.method_lett == 'True':
            for keys, values in self.parser.items("paths letters"):
                self.list_path_lett.update({str(keys):str(values)})

        elif self.method_ext == 'True':
            for k, v in self.parser.items("paths extension"):
                self.list_path_ext.update({str(k): str(v)})
        print(self.list_path_lett)

    def browse_folder(self):
        for keys in self.list_path_ext.items():
            self.list_file.update()
            

            
                
sorter = sorting()
sorter.get_info_config_ini()




            
        
        



            



                    
            


