'''
def combine_letter(text1, text2, i, j):


    find the combination of letters. If there is a space or a period, then it will be 
    a word or sentance and it will move onto the next letter. We will ignolage all 
    other characters but may not have a symbol for them.


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
'''

#! IDK why this def is having a fit!#
def combine_letter_in_line(blue_line, red_line):

    list_of_letters = []
    for i in range(len(blue_line)):
        for j in range(len(red_line)):
            bchar, bc = char_find(blue_line, i)
            rchar, rc = char_find(red_line, j)
            
            while not bc or not rc: #*while both are not true
                #? check to make sure that the characters are a letter. 
                match (bc, rc):
                    case (False, True):  # for Blue
                        i += 1
                        bchar, bc = char_find(blue_line, i)

                    case (True, False):  # for Red
                        j += 1
                        rchar, rc = char_find(red_line, j)

                    case (False, False):  # for Both
                        i += 1
                        j += 1
                        bchar, bc = char_find(blue_line, i)
                        rchar, rc = char_find(red_line, j)

    return list_of_letters
    
def char_find(text, i):
    char, c = text[i], text[i].isalpha()
    return char, c