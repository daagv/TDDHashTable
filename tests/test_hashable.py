import sys
sys.path.append('/Users/xyz/Desktop/code/TDDHashTable/src/')
from hashtable import HashTable

def test_create_hashtable():
    assert HashTable() is not None
