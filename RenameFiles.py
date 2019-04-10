import glob
import os
import sys


class fileNamer():
    #Prompt user for inputs and store in variables
    dir = input("Enter file directory: ")
    old_text = input("Enter old text of file to replace: ")
    new_text = input("Enter new text to replace old text with: ")
    while True:
        try:
            start_num = int(input("Enter file number to start: "))
        except ValueError:
            print("Input must be a number, please try again")
            continue
        else:
            break
    file_extension = input("Enter file extension: ")

    #Check if directory exists, if not try again
    while(os.path.exists(dir)==False):
        print("I did not find the file at, "+str(dir), "\nPlease Try again...")
        dir = input("Enter file directory: ")

    #Check if old_text is in any files
    for filename in os.listdir(dir):
        while(filename.startswith(old_text) == False):
            print("None of the detected files start with ",old_text,"\nPlease Try again")
            old_text = input("Enter old text of file to replace: ")

    #Check if start_num is valid


    #Print files in directory
    print("Files detected: \n",os.listdir(dir))

    #Rename files
    print("Attempting to rename files... ")
    for filename in os.listdir(dir):
        if filename.startswith(old_text):
            src = os.path.join(dir, filename)
            dest = os.path.join(dir, new_text+str(start_num)+file_extension)
            os.rename(src, dest)
        start_num +=1

    print("Files successfully renamed: \n",os.listdir(dir))
    
class main():
    fileNamer()


