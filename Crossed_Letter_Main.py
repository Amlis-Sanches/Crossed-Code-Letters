'''
Crossed Letter Image Generator v0.2.3
Last edit made by: Nathaniel Horn
#------------------------------------------------------------------------------#
This Python script is designed to transform text from various file formats 
(text, Word, PDF) into a 'Crossed Letter' image or document. The process involves:

Inputs:
- File path of the text source.
- File type (text, word, pdf).

Steps:
1. Extract text from the input file.
2. Clean the extracted text for processing.
3. Generate an image or document where:
   a. The first set of text runs left to right in blue.
   b. The document/image is then rotated 90 degrees.
   c. A second set of text is overlaid in red.
   d. Where texts overlap, the colors blend to create purple.
4. Save the output as an image or document.

Desired Output:
A Crossed Letter image or document with the specified text, saved in the user's system.
The image will have the first set of text running left to right in blue, and the second
set of text running top to bottom in red. Where the texts overlap, the colors will blend
to create purple.

'''

# Import necessary libraries
import docx
import PyPDF2
import math
from PIL import Image, ImageDraw, ImageFont, ImageChops

'''
Main function to handle the workflow.


Here i will recieve the text varables in a list and then pass them through the generate_crossed_letter function. 
'''
def main():
    # Get file path and type from user
    # Validate filetype and if wrong file type is entered, ask again
    while True:
        file_path = input("Enter the file path: ")
        file_type = input("Enter the file type (text/word/pdf): ")
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
        print(blue_list[i], "\n", "\n", red_list[i])
        generate_crossed_letter(blue_list[i], red_list[i], i)
    
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
            case "pdf":
                pdf_file = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                full_text = []
                for page in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(page)
                    full_text.append(page_obj.extractText())
                text = "\n".join(full_text)
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

'''
The generate_crossed_letter function is designed to create an image that 
displays two layers of text in different colors (blue and red) overlaid 
in a "crossed letter" style

Create a new merg branch since merg cannot be done in the main function.
'''
def generate_crossed_letter(text1, text2, num_of_images):
    # Create new images for each layer of text
    img1 = Image.new('RGB', (500, 500), color = (255, 255, 255)) #for testing
    img2 = Image.new('RGB', (500, 500), color = (255, 255, 255)) #for testing
    draw1 = ImageDraw.Draw(img1)
    draw2 = ImageDraw.Draw(img2)

    # Select a font
    font = ImageFont.load_default()

    # Add first layer of text in blue
    draw1.text((10, 10), text1, fill=(0, 0, 255), font=font)

    # Rotate the first image
    img1 = img1.rotate(90, expand=1)

    # Add second layer of text in red
    draw2.text((10, 10), text2, fill=(255, 0, 0), font=font)

    # Merge the two images
    img = ImageChops.add(img1, img2)

    # Save the image
    img.save('crossed_letter_purple_' + str(num_of_images) + '.png')

    # Create a new image with the red and blue text on one image. 
    img = Image.new('RGB', (500, 500), color = (255, 255, 255)) #for testing
    draw = ImageDraw.Draw(img)

    # Select a font
    font = ImageFont.load_default()

    # Add first layer of text in blue
    draw.text((10, 10), text1, fill=(0, 0, 255), font=font)

    # Rotate the image
    img = img.rotate(90, expand=1)

    # Create a new drawing context for the rotated image
    draw = ImageDraw.Draw(img)

    # Add second layer of text in red
    draw.text((10, 10), text2, fill=(255, 0, 0), font=font)

    # Save the image
    img.save('crossed_letter_' + str(num_of_images) + '.png')
    
    # Open the two images
    img1 = Image.open('crossed_letter_' + str(num_of_images) + '.png')
    img2 = Image.open('crossed_letter_purple_' + str(num_of_images) + '.png')

    # Blend the images
    blended = Image.blend(img1, img2, alpha=0.5)

    # Save the result
    blended.save('blended_' + str(num_of_images) + '.png')

if __name__ == "__main__":
    main()
