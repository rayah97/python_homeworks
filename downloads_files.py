import os


#Name: get_downloads_folder
#Return: the path to the user's Downloads folder.
def get_downloads_folder():

    return os.path.expanduser("~/Downloads")


#Name: get_file_extension
#Inputs: filename
#Return:  the file extension of the given file name.
def get_file_extension(filename):

    return os.path.splitext(filename)[1]

#Name: skip_non_ext_files
#Inputs: extension
#Return: Skips directories and files without extensions.

def skip_non_ext_files(extension):
    return not extension


#Name: create_subfolder
#Brief: Creates a new subfolder with the given name if it doesn't already exist.
def create_subfolder(subfolder):

    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

#Name: move_file_to_subfolder
#Inputs: file sourse folder, file destination folder
#Brief: Moves a file from the source path to the destination path.
def move_file_to_subfolder(source, destination):

    os.rename(source, destination)


#Name: move_file_to_subfolder
#Brief:  Sorts the files in the user's Downloads folder by file extension and moves them to new subfolders with the same extension name.
def organize_downloads():
   
    downloads_folder = get_downloads_folder()

    for filename in os.listdir(downloads_folder):
        extension = get_file_extension(filename)

        if skip_non_ext_files(extension):
            continue

        subfolder = os.path.join(downloads_folder, extension[1:].upper())
        create_subfolder(subfolder)

        source = os.path.join(downloads_folder, filename)
        destination = os.path.join(subfolder, filename)
        move_file_to_subfolder(source, destination)


def main():
  
    organize_downloads()
    print("Downloads folder organized.")

if __name__ == "__main__":
    main()