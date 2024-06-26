
# Import necessary libraries
import sys
import docx
import math
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageChops
import text_functions as tf
import crossed_letter_functions as clf
import symbol_checker as sc
import Symbols_Generator as sg


'''
Section to check and make sure the images are in tact and not missing. 
If missing it will generate the needed items prior to running code.
Wanted to do this prior to the start of the code to reduce the amount 
of errors that could occur.
'''

check = sc.check_directory()
if check == False:
    print(f'Error: dictorary incomplete needing to run a evaluation and rebuild.')
    answer = input('rebuild Y or N?').lower()
    if answer == 'y':
        sg.main()
    else:
        sys.exit()


'''
Main function to handle the workflow.
'''

def main():
    file_path = input("Enter the file path: ") #get file path from user
    text = tf.extract_text(file_path) #use extraction function from the text_clean
    textCleaned = tf.clean_text(text) #Clean the text to remove unwanted items. 
    blue_list, red_list, num_of_images = tf.group_text(textCleaned)

    # Generate crossed letter
    for i in range(num_of_images):
        tf.combine_letter(blue_list[i], red_list[i], i) #! Evaluate if you want to feed lines or whole paragraphs. Both are posible. !#
    
    print("Crossed Letter Generated!")


if __name__ == "__main__":
    main()