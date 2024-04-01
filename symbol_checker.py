import os
import csv
import sys

# Specify the directory you want to scan
directory = r'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\Photos Generated'

def list_directory(directory):
    # Get a list of all file names in the directory
    file_names = os.listdir(directory)

    # Open a new CSV file in write mode
    with open('Directory.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the list of file names to the CSV file
        for name in file_names:
            writer.writerow([name])

def check_directory(directory, file_list):
    # Get a list of all file names in the directory
    directory_files = os.listdir(directory)

    # Sort both lists before comparing
    directory_files.sort()
    file_list.sort()

    # Compare the lists
    if directory_files == file_list:
        return True
    else:
        return False



if __name__ == '__main__':
    if sys.argv[1] == 'list':
        list_directory(directory)
    elif sys.argv[1] == 'check':
        check_directory(directory, )
    else:
        print('Invalid command. Need aditional argument after text.py document. EX: python text.py list or python text.py check')
        sys.exit()