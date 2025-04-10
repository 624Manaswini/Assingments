import glob
import os

def max_size(directory):
    max_size = 0
    file_name = ''
    for root, dirs, files in os.walk(directory):
            for file in files:
                path = os.path.join(root,file)
                size = os.path.getsize(path)
                if size > max_size:
                    max_size = size
                    file_name = file
    return file_name               
    
print(max_size(r'C:\Users\Mishra\handson'))

