"""
Author: Francisco Hernandez JR
Filename: box_tests.py
Description: Testing the Box class.
"""

import pytest
import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from box import Box

# Fixture for an empty Box
@pytest.fixture
def empty_box():
    # Create a new Box instance
    return Box()

# Fixture for a Box with some entries
@pytest.fixture
def filled_box():
    # Create a new Box instance and add entries
    box = Box()
    box.add("nick1", "species1")
    box.add("nick2", "species2")
    return box

# Test adding a new Entry
@pytest.mark.add
def test_add_new_entry(empty_box):
    # Add a new entry and check if it was added successfully
    assert empty_box.add("nick1", "species1") == True

# Test adding an existing Entry
@pytest.mark.add
def test_add_existing_entry(filled_box):
    # Try to add an entry with an existing nickname
    assert filled_box.add("nick1", "species1") == False

# Test finding an existing Entry
@pytest.mark.find
def test_find_existing_entry(filled_box):
    # Find an existing entry and check if it matches
    entry = filled_box.find("nick1", "species1")
    # Check if the entry was found
    assert entry is not None
    assert entry._Entry__nickname == "nick1"
    assert entry._Entry__species == "species1"

# Test finding a non-existent Entry
@pytest.mark.find
def test_find_nonexistent_entry(filled_box):
    # Try to find a non-existent entry
    assert filled_box.find("nick3", "species3") is None

# Test finding all nicknames
@pytest.mark.findAllNicknames
def test_find_all_nicknames(filled_box):
    # Get all nicknames from the filled_box
    compare_nicknames = Box()
    # Add the same entries to compare_nicknames
    compare_nicknames.add("nickname1", "species1")
    compare_nicknames.add("nickname2", "species2")
    # Verify that the number of nicknames matches
    assert len(filled_box.findAllNicknames()) == len(compare_nicknames.findAllNicknames())

# Test finding all nicknames in an empty Box
@pytest.mark.findAllNicknames
def test_find_all_nicknames_empty_box(empty_box):
    # Get all nicknames from the empty_box
    compare_nicknames = Box()
    # Verify that the number of nicknames matches
    assert len(empty_box.findAllNicknames()) == len(compare_nicknames.findAllNicknames())

# Test finding an Entry by Nickname
@pytest.mark.findEntryByNickname
def test_find_entry_by_nickname(filled_box):
    # Find an existing entry by nickname
    entry = filled_box.findEntryByNickname("nick1")
    # Check if the entry was found
    assert entry is not None
    assert entry._Entry__nickname == "nick1"
    assert entry._Entry__species == "species1"

# Test finding a non-existent Entry by Nickname
@pytest.mark.removeByNickname
def test_remove_by_nickname(filled_box):
    # Remove an existing entry by nickname
    assert filled_box.removeByNickname("nick1") == True
    assert filled_box.findEntryByNickname("nick1") is None

# Test removing a non-existent Entry by Nickname
@pytest.mark.removeByNickname
def test_remove_nonexistent_by_nickname(filled_box):
    # Try to remove a non-existent entry by nickname
    assert filled_box.removeByNickname("nick3") == False

# Test removing an Entry by Nickname and Species
@pytest.mark.removeEntry
def test_remove_entry(filled_box):
    # Remove an existing entry by nickname and species
    assert filled_box.removeEntry("nick2", "species2") == True
    assert filled_box.findEntryByNickname("nick2") is None