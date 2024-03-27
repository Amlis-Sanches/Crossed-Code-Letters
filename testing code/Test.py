import sys
sys.path.append("..")
import text_functions as tf

text1 = 'Hello world h o w a r e you'
text2 = 'This is a test'


def test_countchar():
    assert tf.countchar(text1, 19) == 27
    assert tf.countchar(text2, 11) == 14


def test_clean_text():
    ...

def test_extract_text():
    ...

