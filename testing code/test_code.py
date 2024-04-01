from coded_image_generator import combine_letter

text1 = "Hello World."
text2 = "I am nathan."

def test_combined_letter():
    assert combine_letter(text1, text2, 1, 1) == ("H", "I", False, True, False, False, 1, 1)
    assert combine_letter(text1, text2, 2, 2) == ("e", "a", False, False, False, False, 2, 3)
    assert combine_letter(text1, text2, 3, 3) == ("l", "a", False, False, False, False, 3, 3)
    assert combine_letter(text1, text2, 4, 4) == ("l", "m", False, False, False, False, 4, 4)
    assert combine_letter(text1, text2, 6, 6) == ("W", "n", False, True, False, False, 7, 6)
