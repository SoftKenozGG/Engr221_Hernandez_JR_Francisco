"""
Author: Francisco Hernandez JR
Filename: hashmap_tests.py
Description: Test all functions in myHashMap.py.
"""

import pytest

import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myHashMap import MyHashMap

# Fixture for an empty MyHashMap
@pytest.fixture
def empty_hashmap():
    return MyHashMap()

# Fixture for a MyHashMap filled to various extents
@pytest.fixture
def noloadfactor_hashmap():
    hashmap= MyHashMap()

    # Fill the hashmap without exceeding load factor
    for i in range(10):
        hashmap.put(f"key{i}", f"value{i}")
    return hashmap

# Fixture for a MyHashMap that exceeds load factor
@pytest.fixture
def loadfactor_hashmap():
    hashmap= MyHashMap()

    # Fill the hashmap to exceed load factor
    for i in range(20):
        hashmap.put(f"key{i}", f"value{i}")
    return hashmap # Exceed load factor to trigger resize

# Fixture for a MyHashMap with a large number of elements
@pytest.fixture
def big_hashmap():
    hashmap= MyHashMap()

    # Fill the hashmap with many elements
    for i in range(100):
        hashmap.put(f"key{i}", f"value{i}")
    return hashmap

# Fixture for a MyHashMap that is filled to a certain extent
@pytest.fixture
def filled_hashmap():
    hashmap= MyHashMap()

    # Fill the hashmap with some elements
    for i in range(1, 12):
        hashmap.put(f"key{i}", f"value{i}")
    return hashmap

# Test put method
@pytest.mark.put
# Test adding to an empty hashmap
def test_put_empty_hashmap(empty_hashmap):
    assert empty_hashmap.put("key1", "value1") == True

# Test adding to a hashmap without exceeding load factor
@pytest.mark.put
def test_put_no_loadfactor(noloadfactor_hashmap):
    assert noloadfactor_hashmap.put("key11", "value11") == True # This should not trigger a resize

# Test adding to a hashmap that exceeds load factor
@pytest.mark.put
def test_put_loadfactor(loadfactor_hashmap):
    assert loadfactor_hashmap.put("key21", "value21") == True # This should trigger a resize

# Test adding a key that already exists
@pytest.mark.put
def test_put_key_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.put("key5", "new_value") == False

# Test replace method
@pytest.mark.replace
# Test replacing value for an existing key
def test_replace_key_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.replace("key3", "new_value3") == True
    assert noloadfactor_hashmap.get("key3") == "new_value3"

# Test replacing value for a non-existing key
@pytest.mark.replace
def test_replace_key_not_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.replace("key_not_exist", "value") == False

# Test remove method
@pytest.mark.remove
# Test removing an existing key
def test_remove_key_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.remove("key4") == True
    assert noloadfactor_hashmap.containsKey("key4") == False

# Test removing a non-existing key
@pytest.mark.remove
def test_remove_key_not_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.remove("key_not_exist") == False

# Test set method
@pytest.mark.set
# Test setting value for an existing key
def test_set_key_exists(noloadfactor_hashmap):
    noloadfactor_hashmap.set("key2", "updated_value2")
    assert noloadfactor_hashmap.get("key2") == "updated_value2"

# Test setting value for a non-existing key
@pytest.mark.set
def test_set_key_not_exists(noloadfactor_hashmap):
    noloadfactor_hashmap.set("key_not_exist", "new_value")
    assert noloadfactor_hashmap.get("key_not_exist") == "new_value"

# Test get method
@pytest.mark.get
# Test getting value for an existing key
def test_get_key_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.get("key1") == "value1"

# Test getting value for a non-existing key
@pytest.mark.get
def test_get_key_not_exists(noloadfactor_hashmap):
    assert noloadfactor_hashmap.get("key_not_exist") == None

# Test get_size method
@pytest.mark.get_size
# Test getting size for an empty hashmap
def test_size_empty_hashmap(empty_hashmap):
    assert empty_hashmap.get_size() == 0

# Test getting size for a small hashmap
@pytest.mark.get_size
def test_size_small_hashmap():
    small_size_hashmap = MyHashMap()
    small_size_hashmap.put("key1", "value1")
    assert small_size_hashmap.get_size() == 1

# Test getting size for a big hashmap
@pytest.mark.get_size
def test_size_big_hashmap(big_hashmap):
    assert big_hashmap.get_size() == 100

# Test isEmpty method
@pytest.mark.isEmpty
# Test isEmpty on an empty hashmap
def test_isEmpty_empty_hashmap(empty_hashmap):
    assert empty_hashmap.isEmpty() == True

# Test isEmpty on a filled hashmap
@pytest.mark.isEmpty
def test_isEmpty_filled_hashmap(filled_hashmap):
    assert filled_hashmap.isEmpty() == False

# Test containsKey method
@pytest.mark.containsKey
# Test containsKey for an existing key
def test_containsKey_key_exists(filled_hashmap):
    assert filled_hashmap.containsKey("key6") == True

# Test containsKey for a non-existing key
@pytest.mark.containsKey
def test_containsKey_key_not_exists(filled_hashmap):
    assert filled_hashmap.containsKey("key_not_exist") == False

# Test keys method
@pytest.mark.keys
# Test keys on an empty hashmap
def test_keys_empty_hashmap():
    empty_hashmap = MyHashMap()
    assert empty_hashmap.keys() == []

# Test keys on a filled hashmap
@pytest.mark.keys
def test_keys_non_empty_hashmap(filled_hashmap):
    keys = filled_hashmap.keys()
    # Verify all expected keys are present
    expected_keys = [f"key{i}" for i in range(1, 12)]
    # Check that all expected keys are in the returned keys
    for key in expected_keys:
        # Check that the key is in the returned keys
        assert key in keys