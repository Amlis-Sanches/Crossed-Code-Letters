import os
import csv
import sys

# Specify the directory you want to scan
default_directory = r'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\Symbols Images'

# Specify a full path for the CSV file
csv_file_path = r'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\Directory.csv'

def list_directory(directory = default_directory):
    # Get a list of all file names in the directory
    file_names = os.listdir(directory)

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the list of file names to the CSV file
        for name in file_names:
            writer.writerow([name])

def check_directory(directory = default_directory):
    # Get a list of all file names in the directory
    directory_files = os.listdir(directory)
    file_list = read_csv_to_list(csv_file_path)


    # Sort both lists before comparing
    directory_files.sort()
    file_list.sort()

    # Compare the lists
    if directory_files == file_list:
        return True
    else:
        return False


def read_csv_to_list(csv_file_path):
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]



if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'list':
            list_directory(directory)
            print(f'directory list created. Location: {read_csv_to_list}')
        elif sys.argv[1] == 'check':
            print(f'The files were reviewed and the directory being in contact was found to be {check_directory(directory)}.')  # Outputs: True or False
        else:
            print('Invalid command. Additional argument after script name needs to be list or check. EX: python script.py list or python script.py check')
            sys.exit()
    else:
        print("No command provided. Need additional argument after script name. EX: python script.py list or python script.py check")
        sys.exit()
