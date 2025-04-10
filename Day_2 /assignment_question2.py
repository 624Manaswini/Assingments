# Ruecursively go below a dir and based on filter, dump those files in to a single file (work with only text file)

def dump_file_filterBased(directory, res_file):
    with open(res_file,'w') as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.txt'):
                    path = os.path.join(root,file)
                    with open(path, 'r') as f1:
                        f.write(f"content of file : {path}")
                        f.writelines(f1.readlines())

dump_file_filterBased(r'C:\Users\Mishra\handson', 'dump_file.txt')
