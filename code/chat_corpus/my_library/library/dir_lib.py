import os

# create one single directory
def create_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if(e.errno != errno.EEXIST):
            raise
    pass 


# create a list of directories
def create_directories(list_dir):
    for dir_i in list_dir:
        print(dir_i)
        create_directory(dir_i) 
        
        
# delete one single directory
def delete_directory(dir_name):
    if(os.path.isdir(dir_name)):
        try:
            shutil.rmtree(dir_name)
        except OSError as e:
            if(e.errno != errno.EEXIST):
                raise
        pass 

    
# delete a list of directories
def delete_directories(list_dir):
    for dir_i in list_dir:
        print(dir_i)
        delete_directory(dir_i)

        
#delete if file is empty
def delete_file(path):
    try:
        os.remove(path)
    except WindowsError:
        print("failed deleting: " + path)
        pass
        
