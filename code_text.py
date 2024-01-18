
# Import necessary libraries
import docx
import math
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageChops

'''
Main function to handle the workflow.
'''

def main():
    # Get file path and type from user
    # Validate filetype and if wrong file type is entered, ask again
    while True:
        file_path = input("Enter the file path: ")
        file_type = input("Enter the file type (text/word): ")
        if file_type in ["text", "word", "pdf"]:
            #try to confirm and extract text from file
            text = extract_text(file_path, file_type)
            if text == "Error":
                print("File Error extracting text. Please try again.")
            else:
                break
        elif file_type == "exit":
            print("Good Bye!")
            exit()
        else:
            print("Invalid file type. Please try again.")
    '''
    clean text for generation and return two lists filled with the text string variables.
    I create the list inside the function because I want to have everything formed befor 
    I pass it to the generate_crossed_letter function.
    '''
    blue_list, red_list, num_of_images = text_clean(text)

    # Generate crossed letter
    for i in range(num_of_images):
        combine_letter(blue_list[i], red_list[i], i)
    
    print("Crossed Letter Generated!")


# Function to extract text from various formats
def extract_text(file_path, file_type):
    # Identify file type. If text, return text
    try:
        match file_type:
            case "text":
                with open(file_path, "r") as file:
                    text = file.read()
            case "word":
                doc = docx.Document(file_path)
                full_text = []
                for para in doc.paragraphs:
                    full_text.append(para.text)
                text = "\n".join(full_text)
                '''
            case "pdf":
                pdf_file = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                full_text = []
                for page in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(page)
                    full_text.append(page_obj.extractText())
                text = "\n".join(full_text)
                '''
            case _:
                text = "Program Error"
    except:
        text = "Error! Document not identified. Please try again."
    #return just a string with all the text from the file
    return text
    
def text_clean(text):
    # Clean text for generation
    cleaned_text = text.replace('\n', '')
    cleaned_text = cleaned_text.replace('\t', '')
    
    
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

def combine_letter(text1, text2, i, j):
    '''
    find the combination of letters. If there is a space or a period, then it will be 
    a word or sentance and it will move onto the next letter.
    '''
    match text1[i], text2[i]:
        case (" ", " "):
            B_letter = text1[i+1]
            R_letter = text2[j+1]
            i, j = i+1, j+1
        case (".", "."):
            B_letter = text1[i+1]
            R_letter = text2[j+1]
            i, j = i+1, j+1
        case (" ", _):
            B_letter = text1[i+1]
            R_letter = text2[j]
            i += 1
        case (".", _):
            B_letter = text1[i+1]
            R_letter = text2[j]
            i += 1
        case (_, " "):
            B_letter = text1[i]
            R_letter = text2[j+1]
            j += 1
        case (_, "."):
            B_letter = text1[i]
            R_letter = text2[j+1]
            j += 1
        case _:
            B_letter = text1[i]
            R_letter = text2[j]

    match text1[i+1], text2[i+1]:
        case (" ", " "):
            B_word = True
            R_word = True
        case (".", "."):
            b_sentance = True
            r_sentance = True
        case (" ", _):
            B_word = True
            R_word = False
        case (".", _):
            b_sentance = True
            r_sentance = False
        case (_, " "):
            B_word = False
            R_word = True
        case (_, "."):
            b_sentance = False
            r_sentance = True
        case _:
            B_word = False
            R_word = False
            b_sentance = False
            r_sentance = False
    return B_letter, R_letter, B_word, R_word, b_sentance, r_sentance, i, j



if __name__ == "__main__":
    main()