import os

def create_output_folder():
    
    folder_name = "output"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Output folder created")

    else:
        print("Output folder already exists")

    return folder_name