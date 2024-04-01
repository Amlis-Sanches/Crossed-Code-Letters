'''
This code is an example code to explain how i came to the conclusion of how many posible combinations there are for combining
two letters in the alphabet. 

It was found that there is going to be a generation of 325 images and it be better to have Python generate these images than for me
to make them by hand.
'''
import math
combinations_of_letters = 26**2
end_of_word = combinations_of_letters * 4
end_of_sentence = end_of_word * 4
print(end_of_sentence)



