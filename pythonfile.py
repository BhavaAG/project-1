import pytest

from main import Subclass

obj = Subclass('textfile.txt','output.txt')

@pytest.mark.test1
def test_prefix():
    assert obj.prefix() != -1

def test_suffix():
    assert obj.suffix() == 3

def test_max_num():
    assert obj.max_num() ==  'singing'

def test_palindrome():
    assert obj.palindrome() != 'Null'

def test_uniquename():
    assert obj.uniquename() == []

