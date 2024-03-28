
# Import necessary libraries
import docx
import math
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageChops
import text_functions as tf

'''
Main function to handle the workflow.
'''

def main():
    file_path = input("Enter the file path: ") #get file path from user
    text = tf.extract_text(file_path) #use extraction function from the text_clean
    textCleaned = tf.clean_text(text) #Clean the text to remove unwanted items. 
    blue_list, red_list, num_of_images = tf.group_text(textCleaned) # !! determine how to operate !!#

    # Generate crossed letter
    for i in range(num_of_images):
        tf.combine_letter(blue_list[i], red_list[i], i)
    
    print("Crossed Letter Generated!")


if __name__ == "__main__":
    main()