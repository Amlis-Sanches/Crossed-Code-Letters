import math
import docx
import re
import num2words

def main():
    file_path = 'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\File Examples\Story_example.txt'
    text = extract_text(file_path)
    blue_list, red_list, num_of_images = text_clean(text)

def extract_text(file_path):
    # Identify file type. If text, return text
    try:
        match = re.search(r'\.(\w+)$', file_path)
        file_type = match.group(1) if match else None
        
        match file_type:
            case "txt":
                with open(file_path, "r") as file:
                    text = file.read()

            case "docx":
                doc = docx.Document(file_path)
                full_text = []
                for para in doc.paragraphs:
                    full_text.append(para.text)
                text = "\n".join(full_text)
                
            case _:
                text = "Program Error"
    except:
        text = "Error! Document not identified. Please try again."
    #return just a string with all the text from the file
    return text

def text_clean(text):
    # Convert all numbers into words. Do this first to reduce glitches
    text = re.sub(r'\b\d+\b', lambda x: num2words(int(x.group())), text)


    # remove all new lines and tabs
    char_list = ['\n', '\t', '\r', '"', '“', '”', '‘', '’', "'"] # List of characters to remove
    for char in char_list:
        text = text.replace(char, '')


    # Shape test to fit for the desired image
    for i in range(0, len(cleaned_text), 80):
        if i + 1 < len(cleaned_text):  # Ensure i+1 is a valid index
            if cleaned_text[i] in ' .,?!:;':
                cleaned_text = cleaned_text[:i] + '\n' + cleaned_text[i:]
            elif (cleaned_text[i].isalpha() or cleaned_text[i] == "'") and cleaned_text[i+1] in " .,?!:;'":
                cleaned_text = cleaned_text[:i+1] + '\n' + cleaned_text[i+1:]
            elif (cleaned_text[i].isalpha() or cleaned_text[i] == "'") and (cleaned_text[i].isalpha() or cleaned_text[i] == "'"):
                for j in range(i, max(0, i-80), -1):  # Iterate backwards from i
                    if cleaned_text[j] == ' ':
                        cleaned_text = cleaned_text[:j] + '\n' + cleaned_text[j+1:]
                        i = i-j
                        break  # Exit the loop once a space is found


    # Check if the last line is longer than 80 characters
    last_newline = cleaned_text.rfind('\n')
    if len(cleaned_text) - last_newline > 80:
        for j in range(len(cleaned_text), last_newline, -1):
            if cleaned_text[j] == ' ':
                cleaned_text = cleaned_text[:j] + '\n' + cleaned_text[j+1:]
                break  # Exit the loop once a space is found


    # Count the total number of lines and determine how many images will be processed
    total_lines = len(cleaned_text.split('\n'))
    # split lines after you reach 32 lines so the \n fits the image
    half_length = 30 #Set to a specific number to fit the desired image
    total_image = round(total_lines // (half_length * 2))


    #create a red and blue list to hold the text
    total_image = math.ceil(total_lines / (half_length * 2))
    blue_list = [''] * total_image
    red_list = [''] * total_image


    cleaned_text_lines = cleaned_text.split('\n')
    counter = 0
    for i in range(0, len(cleaned_text_lines), (half_length*2)):
        if i % half_length == 0:
            blue_list[counter] = '\n'.join(cleaned_text_lines[:half_length])
            red_list[counter] = '\n'.join(cleaned_text_lines[half_length:])
            counter += 1
        cleaned_text_lines = cleaned_text_lines[(half_length*2):]
    return blue_list, red_list, total_image