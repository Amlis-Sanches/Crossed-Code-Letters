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
#! Split this function into two functions and prep for testing!#
def combine_letter_in_line(blue_line, red_line):

    for i in range(len(blue_line)):
        for j in range(len(red_line)):
            bchar, bc = char_find(blue_line, i)
            rchar, rc = char_find(red_line, j)
            bchar, bc, i, rchar, rc, j = letter_check(blue_line, red_line, bc, rc, i, j)
            
            #TODO check if there is a space or a period+ icon and identify the end of a sentance for both red and blue
            #TODO store the information for one item into a list for the output
            
            z, k = i + 1, j + 1
            B = blue_line[z]
            R = red_line[k]

            variables = {'B': {}, 'R': {}}
            for next_char in [('B', blue_line[z]), ('R', red_line[k])]:
                name, char = next_char
                match char:
                    case '.'|'!'|'?':
                        variables[name]['sentence'] = True
                        variables[name]['word'] = True
                    case ' ':
                        variables[name]['sentence'] = False
                        variables[name]['word'] = True
                    case _ :
                        variables[name]['sentence'] = False
                        variables[name]['word'] = False
                
                
                ''' Example code as a note for the future
                print(variables['B']['sentence'])  # Prints the value of Bsentence
                print(variables['R']['word'])  # Prints the value of Rword
                '''
            
    return variables

def letter_check(blue_line, red_line , bc, rc, i, j):
    #* check if the characters are letters
    while not bc or not rc: #*while both are not true
        match (bc, rc):
            case (False, True):  # for Blue
                i += 1
                bchar, bc = char_find(blue_line, i)
                return bchar, bc, i, rchar, rc, j

            case (True, False):  # for Red
                j += 1
                rchar, rc = char_find(red_line, j)
                return bchar, bc, i, rchar, rc, j

            case (False, False):  # for Both
                i += 1
                j += 1
                bchar, bc = char_find(blue_line, i)
                rchar, rc = char_find(red_line, j)
                return bchar, bc, i, rchar, rc, j

def char_find(text, i):
    char, c = text[i], text[i].isalpha()
    return char, c