from code_text import combine_letter

text1 = "Hello World."
text2 = "I am nathan."

def test_combined_letter():
    assert combine_letter(text1, text2, 1, 1) == ("H", "I", False, True, False, False)
    assert combine_letter(text1, text2, 2, 2) == ("e", "a", False, False, False, False)
