import os

def mkdir(file_dir):
    isExists = os.path.exists(file_dir)
    if not isExists: 
        os.makedirs(file_dir)
        print("file make direction sucessfully!")
    else: 
        print("file has already exists!")