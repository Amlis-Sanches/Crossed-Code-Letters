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
import num2words
import sys
import pandas as pd


def main():
    file_path = r'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\File Examples\Story_example.txt'
    text = extract_text(file_path)
    blue_list, red_list, num_of_images = text_clean(text)


def extract_text(file_path):
    # Identify file type. If text, return text
    try:
        match = re.search(r"\.(\w+)$", file_path)
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
                print("Program Error, unadentified document type. Please try again.")
                sys.exit()
    except:
        print("Error! Document unable to be processed")
        sys.exit()
    # return just a string with all the text from the file
    return text


def text_clean(text):
    # Convert all numbers into words. Do this first to reduce glitches
    text = re.sub(r"\b\d+\b", lambda x: num2words(int(x.group())), text)

    # remove all new lines and tabs
    char_list = [
        "\n",
        "\t",
        "\r",
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
        cleaned_text = text.replace(char, "")

    location = countchar(cleaned_text, 80)
    # using the determined number of characters, insert a new line after that character.
    for i in range(0, len(cleaned_text), location):
        # rest of your code
        location = countchar(cleaned_text, 80)
        grouptext = cleaned_text[:i] + "\n" + cleaned_text[i:]

        """ Removed from code since this is fixed with the function countchar
        if i + 1 < len(cleaned_text):  # Ensure i+1 is a valid index
            if cleaned_text[i] in ' .,?!:;':
                cleaned_text = cleaned_text[:i] + '\n' + cleaned_text[i:]
            elif cleaned_text[i].isalpha() and cleaned_text[i+1] in " .,?!:;":
                cleaned_text = cleaned_text[:i+1] + '\n' + cleaned_text[i+1:]
            else:
                cleaned_text = cleaned_text[:i] + '\n' + cleaned_text[i:]
        """

    """ Can remove since the length of 80 count is needed since we identify alphanumeric caracters
    # Check if the last line is longer than 80 characters
    last_newline = cleaned_text.rfind('\n')
    if len(cleaned_text) - last_newline > 80:
        for j in range(len(cleaned_text), last_newline, -1):
            if cleaned_text[j] == ' ':
                cleaned_text = cleaned_text[:j] + '\n' + cleaned_text[j+1:]
                break  # Exit the loop once a space is found
    """

    # Count the total number of lines and determine how many images will be processed
    total_lines = len(cleaned_text.split("\n"))
    # split lines after you reach 32 lines so the \n fits the image
    Image_character_length = (
        30  # Set to a specific length so the character length is 80W by 30L
    )
    total_image = round(total_lines // (Image_character_length * 2))

    # create a red and blue list to hold the text
    total_image = math.ceil(total_lines / (Image_character_length * 2))
    blue_list = [""] * total_image
    red_list = [""] * total_image

    cleaned_text_lines = cleaned_text.split("\n")
    counter = 0
    for i in range(0, len(cleaned_text_lines), (Image_character_length * 2)):
        if i % Image_character_length == 0:
            blue_list[counter] = "\n".join(cleaned_text_lines[:Image_character_length])
            red_list[counter] = "\n".join(cleaned_text_lines[Image_character_length:])
            counter += 1
        cleaned_text_lines = cleaned_text_lines[(Image_character_length * 2) :]
    return blue_list, red_list, total_image


"""
This function counts the number of characters that are alphanumeric and excludes veryhting else. 
The reason for this is so i can remove the if statement of when to add a new line and here i can
keep the other charicters that i need to identify where a dot is placed. 
"""


def countchar(text, maxchar, charlist=[" ", ".","?"]):
    if len(text) < maxchar:
        max = len(text)
    else:
        max = maxchar

    count = 0
    i = 0
    while i < len(text) and count < maxchar:
        character = text[i]
        if character.isalpha():
            count += 1
        elif character in charlist:
            count += 1
        elif character.isnumeric():
            print(f"Error: character {i} was identified as a number: {character}")
            return False
        else:
            print(
                f"{character} is not identified as a possible character to analyze. \nPlease remove character at position {i}"
            )
            return False
        i += 1

    return count
