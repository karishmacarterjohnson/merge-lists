import pytest
from merge_lists import mergeSortTwoLists

def test_example1():
    a = [1,2,4,5]
    b = [6]
    assert mergeSortTwoLists(a,b) == [1,2,4,5,6]

def test_example2():
    a = [-30, -10, 0, 15, 16]	
    b = [-20, -5, 5]	
    assert mergeSortTwoLists(a, b) == [-30, -20, -10, -5, 0, 5, 15, 16]

