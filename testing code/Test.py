import sys
sys.path.append("..")
import text_functions as tf

text1 = 'Hello world h o w a r e you'
text2 = 'This is a test'
text3 = 'Hello1  yes2'
text4 = 'no its % not percent'


def test_countchar():
    assert tf.countchar(text1, 18) == 26
    assert tf.countchar(text2, 11) == 14
    assert tf.countchar(text3,4) == 4
    assert tf.countchar(text3,8) == False
    assert tf.countchar(text4, 3) == 4
    assert tf.countchar(text4, 6) == False


def test_clean_text():
    ...

def test_extract_text():
    ...

