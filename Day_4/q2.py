
import glob
import os
import datetime

class File:

    def __init__(self, directory):
        self.directory = directory
        
    def getMaxSizeFile(self, n):
        def get_max_file(path):
            def get_files(path, ed={}):
                files = glob.glob(os.path.join(path, "*"))
                for f in files:
                    if os.path.isfile(f):
                        ed[f] = os.path.getsize(f)
                    elif os.path.isdir(f):
                        get_files(f, ed)
                return ed
            allfiles = get_files(path)
            std = sorted(allfiles, key=lambda k: allfiles[k], reverse=True)
            return std[:n]
        return get_max_file(self.directory)
        
    
    def getLatestFiles(self,date):
        result = []
        for f in os.listdir(self.directory):
            filepath = os.path.join(self.directory, f)
            if os.path.isfile(filepath):
                last_time = datetime.date.fromtimestamp(os.path.getmtime(filepath))
                if last_time > date:
                    result.append(f)
        return result
                    
fs = File(".")                
print(fs.getMaxSizeFile(2) ) 
print(fs.getLatestFiles(datetime.date(2018,2,1)))            





