import pandas as pd
class File:

    path = None
    file = None

    def __init__(self,path):
        self.path = path

    def uploadFile(self):
        self.file = pd.read_csv(self.path,sep=';')

    def getFile(self):
        return self.file
