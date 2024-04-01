
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