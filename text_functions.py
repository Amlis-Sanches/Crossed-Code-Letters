"""
Summary Description
This Python script is designed to process textual documents, specifically focusing on optimizing the format of the 
text for visual presentation, such as in images. The script supports input files in both plain text (txt) and 
Microsoft Word (docx) formats. The main functionalities of this script include extracting text from the specified 
file, cleaning and formatting the text according to specific rules, and preparing the text for image processing by 
organizing it into a structured format suitable for visual display.

Key Functionalities
Text Extraction: The script identifies the file type based on the file extension and extracts the text accordingly. 
For .txt files, it reads the content directly. For .docx files, it iterates over paragraphs to compile the text.

Text Cleaning and Formatting:
- Converts all numerical values into their word equivalents to maintain a consistent textual format.

- Removes specific unwanted characters and symbols (e.g., newlines, tabs, quotes, punctuation marks) to clean the text.

- Implements a custom function countchar to count the number of alphanumeric characters, excluding others, to 
facilitate precise text formatting.

- Organizes the cleaned text into segments that adhere to a specified character length and line count, aiming for an 
80-character width and 30-line length per segment. This structure is tailored for optimal visual presentation in images.

- Image Preparation: The script calculates the number of images that can be generated based on the total line count 
of the cleaned text. It then divides the text into two lists (blue_list and red_list), each containing segments of text 
formatted for visual presentation. These lists are intended to differentiate text visually, possibly by color or other 
means, in the final images.

Error Handling: It includes basic error handling for file type identification and character analysis, with specific 
checks for alphanumeric characters and a safeguard against unexpected character types.

Detailed Points
- The script employs regular expressions (regex) for identifying file types and for the initial step of converting 
numbers to words within the text.

- It utilizes the docx library to handle .docx files, parsing through each paragraph to compile the document's text.

- The num2words library is used to convert numerical values to their corresponding words, enhancing the text's readability.

- The math library aids in calculating the number of images required based on the text's structure.

- The script's formatting strategy aims to maintain a uniform width of 80 characters and segments the text to fit within 
an image's dimensions, specifically targeting a dimension that can accommodate 30 lines of text per image.

- Custom error messages are implemented to guide users through resolving issues with non-alphanumeric characters and to 
ensure the text is suitable for the intended visual presentation format.
"""

import math
import docx
import re
from num2words import num2words
import sys
import pandas as pd


def main(): #used for testing this code on its own. 
    file_path = r"C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\File Examples\Story_example.txt"
    text = extract_text(file_path)
    text = clean_text(text)
    blue_list, red_list, num_of_images = group_text(text)


def extract_text(file_path):
    # Identify file type. If text, return text
    try:
        match = re.search(r"\.(\w+)$", file_path)
        file_type = match.group(1) if match else None

        if file_type == "txt":
            with open(file_path, "r") as file:
                text = file.read()
        elif file_type == "docx":
            doc = docx.Document(file_path)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            text = "\n".join(full_text)
        else:
            return False
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Extraction did not work: {str(e)}"
    # return just a string with all the text from the file
    return text


def clean_text(text):
    text = text.lower()

    char_list = [
        ",",
        ".",
        "?",
        "!",
        "-",
        "_",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "/",
        "\\",
        "*",
        "^",
        "$",
        "|",
        '"',
        "“",
        "”",
        "‘",
        "’",
        "'",
        ";",
        ":",
    ]  # List of characters to remove
    for char in char_list:
        text = text.replace(char, "")
    
    '''
    this is to review all the numbers and unique symbols in the string and change them to numbers. If a number is larger than 1 character long
    it will be able to identify what number it is. 
    '''

    #create a dic to replace symbols with the word
    replace_dic = {
        '%':'percent',
        '&':'and',
        '=':'equal',
        '+':'plus',
        '-':'minus',
        '<':'less than',
        '>':'greater than',
        '#':'number',
        '@':'at',
        }

    i = 0
    while i < len(text):
        if text[i].isdigit():
            j = i
            while j < len(text) and text[j].isdigit():
                j += 1
            number = int(text[i:j])
            word = num2words(number)
            text = replace_char_with_string(text, i, j, word)
            i += len(word)
        if text[i] in replace_dic:
            word = replace_dic[text[i]]
            text = replace_char_with_string(text,i, i+1, word)
        else:
            i += 1

    return text


def group_text(text, charw = 80, lines = 30):
    location = countchar(text, charw)
    # using the determined number of characters, insert a new line after that character.

    for i in range(0, len(text), location if location != 0 else exit('group_text function for loop')):
        # rest of your code
        location = countchar(text, charw)
        grouptext = replace_char_with_string(text, i, i, '\n')

    # Count the total number of lines and determine how many images will be processed
    total_lines = len(text.split("\n"))

    # split lines after you reach 32 lines so the \n fits the image
    Image_character_length = (
        lines  # Set to a specific length so the character length is 80W by 30L
    )
    
    total_image = round(total_lines // (Image_character_length * 2))

    # create a red and blue list to hold the text
    total_image = math.ceil(total_lines / (Image_character_length * 2))
    blue_list = [""] * total_image
    red_list = [""] * total_image

    text_lines = text.split("\n")
    counter = 0
    for i in range(0, len(text_lines), (Image_character_length * 2)):
        if i % Image_character_length == 0:
            blue_list[counter] = "\n".join(text_lines[:Image_character_length])
            red_list[counter] = "\n".join(text_lines[Image_character_length:])
            counter += 1
        text_lines = text_lines[(Image_character_length * 2) :]
    return blue_list, red_list, total_image


def combine_letter(text1, text2, i, j):
    '''
    find the combination of letters. If there is a space or a period, then it will be 
    a word or sentance and it will move onto the next letter. We will ignolage all 
    other characters but may not have a symbol for them.
    '''
    for character in [".", " ", ",", "?", "!", ":", ";", "-", "'", '"', "_"]:
        if text1[i] == character and text2[j] == character:
            B_letter = text1[i+1]
            R_letter = text2[j+1]
            i, j = i+1, j+1
        elif text1[i] == character and text2[j] != character:
            B_letter = text1[i+1]
            R_letter = text2[j]
            i = i+1
        elif text1[i] != character and text2[j] == character:
            B_letter = text1[i]
            R_letter = text2[j+1]
            j = j+1
        else:
            B_letter = text1[i]
            R_letter = text2[j]

    '''
    Unique characters in a scentance will have a different symbol list.
    '''

    for character in [" ", ",", ";", "-", "'", '"', "_"]:
        if text1[i] == character and text2[j] == character:
            B_word = True
            R_word = True

        elif text1 == character and text2[j] != character:
            B_word = True
            R_word = False

        elif text1[i] != character and text2[j] == character:
            B_word = False
            R_word = True

        else:
            B_word = False
            R_word = False

    '''
    Create a sybmol identification for scentences. Identifying characters that end a sentance.
    '''

    for character in [".", "?", "!"]:
        if text1[i] == character and text2[j] == character:
            b_sentance = True
            r_sentance = True

        elif text1 == character and text2[j] != character:
            b_sentance = True
            r_sentance = False

        elif text1[i] != character and text2[j] == character:
            b_sentance = False
            r_sentance = True

        else:
            b_sentance = False
            r_sentance = False
    
    return B_letter, R_letter, B_word, R_word, b_sentance, r_sentance, i, j

"""
This function counts the number of characters that are alphanumeric and excludes veryhting else. 
The reason for this is so i can remove the if statement of when to add a new line and here i can
keep the other charicters that i need to identify where a dot is placed. 
"""


def countchar(text, maxchar, charlist=[" ", ".", "?", ""]):
    if len(text) < maxchar:
        max = len(text)
    else:
        max = maxchar

    alphachar = 0
    count = 0
    i = 0

    while i < len(text) and alphachar < maxchar:
        character = text[i]

        if character.isalpha():
            # increase the char count and alpha count
            count += 1
            alphachar += 1

        elif character in charlist:
            # just increase the char count since its not an alpha
            count += 1

        elif character.isnumeric():
            print(f"Error: character {i} was identified as a number: {character}")
            return False
        
        elif character == '\n':
            count += 1

        else:
            exit(
                f"{character} is not identified as a possible character to analyze. \nPlease remove character at position {i}"
            )
            return False
        i += 1  # increase the value of i at the end of every test.

    return count


# keeping for future use. if needing to replace specific items it will help out a lot. 
def replace_char_with_string(original_string, index1, index2, new_string):
    # Slice the original string and concatenate with the new string
    new_string = original_string[:index1] + new_string + original_string[index2:]
    return new_string


def exit(location = 'Undefined'):
    print(f'Error: {location}. Exiting code')
    sys.exit()