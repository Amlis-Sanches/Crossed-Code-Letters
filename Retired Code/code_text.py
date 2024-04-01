
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



if __name__ == "__main__":
    main()