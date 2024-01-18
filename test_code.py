from code_text import generate_crossed_letter

def test_generate_crossed_letters():
    assert generate_crossed_letter("blue_list[i]", "red_list[i]", "i") == "Crossed Letter Generated!"