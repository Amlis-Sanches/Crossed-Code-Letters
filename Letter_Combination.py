'''
This code is an example code to explain how i came to the conclusion of how many posible combinations there are for combining
two letters in the alphabet. 

It was found that there is going to be a generation of 325 images and it be better to have Python generate these images than for me
to make them by hand.
'''
import math

# Total number of letters in the English alphabet
n = 26

# Number of letters to select at a time
k = 2

# Calculate the number of combinations using the combinations formula
combinations = math.comb(n, k)

# Print the result
print(f"Number of combinations of {k} letters from the English alphabet: {combinations}")

'''
Explanation:

To determine all possible combinations of 2 letters in the English alphabet, 
you can use combinations without repetition. There are 26 letters in the 
English alphabet, and you want to select 2 of them at a time. The formula 
to calculate the number of combinations is:

C(n, k) = n! / (k! * (n - k)!)

Where:

- C(n, k) represents the number of combinations of selecting k items from n items.
- n! (n factorial) is the product of all positive integers from 1 to n.
- k! (k factorial) is the product of all positive integers from 1 to k.

In this case, n is the total number of letters in the alphabet (26), and k 
is the number of letters you want to select at a time (2).

So, to calculate the number of combinations of 2 letters from the English 
alphabet:

C(26, 2) = 26! / (2! * (26 - 2)!)

C(26, 2) = (26 * 25) / (2 * 1) = 325

There are 325 possible combinations of 2 letters in the English alphabet. 
You can also generate these combinations programmatically using a loop or 
a recursive function if needed.
'''

