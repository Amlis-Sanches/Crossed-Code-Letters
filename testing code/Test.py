import sys
sys.path.append("..")
import text_functions as tf

#for countchar()
text1 = 'Hello world h o w a r e you'
text2 = 'This is a test'
text3 = 'Hello1  yes2'
text4 = 'no its % not percent'

#for clean_text()
t1 = 'A1 2 B3B'
t2 = 'A10 20 B20bb'

#for extract_tect()
file_path = r'C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\File Examples\pytest.txt'

def test_countchar():
    assert tf.countchar(text1, 18) == 26
    assert tf.countchar(text2, 11) == 14
    assert tf.countchar(text3,4) == 4
    assert tf.countchar(text3,8) == False
    assert tf.countchar(text4, 3) == 4
    assert tf.countchar(text4, 6) == False


def test_clean_text():
    assert tf.clean_text(t1) == 'aone two bthreeb'
    assert tf.clean_text(t2) == 'aten twenty btwentybb'


def test_goup_text():
    ...

def test_extract_text():
    assert tf.extract_text(file_path) == 'this is a test'

