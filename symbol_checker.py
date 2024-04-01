import os
import csv

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

def check_directory(directory):
    # Get a list of all file names in the directory
    file_names = os.listdir(directory)



if __name__ == '__main__':
    list_directory(directory)