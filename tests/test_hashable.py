import sys
sys.path.append('/Users/xyz/Desktop/code/TDDHashTable/src/')
from hashtable import HashTable

def test_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None,None,None]
