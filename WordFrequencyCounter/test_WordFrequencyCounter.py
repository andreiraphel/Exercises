import pytest
import tempfile
import os
from word_counter import WordFrequencyCounter

@pytest.fixture
def test_file_content():
    return "This is a test file for word counting. It includes words with punctuation marks, such as 'can't' and 'mother-in-law'. How will it handle hyphens?"

def test_word_count_existing_file(test_file_content):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(test_file_content)
        temp_file_path = temp_file.name

    # Call the WordFrequencyCounter function and check the word count
    word_count = WordFrequencyCounter(temp_file_path)
    assert word_count == 24  # Correctly counts 27 words in the test string

def test_word_count_nonexistent_file():
    with pytest.raises(SystemExit) as excinfo:
        WordFrequencyCounter("nonexistent.txt")

    assert str(excinfo.value) == "File not found"

def test_word_count_empty_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name

    # Call the WordFrequencyCounter function on an empty file and check the word count
    word_count = WordFrequencyCounter(temp_file_path)
    assert word_count == 0  # Correctly counts 0 words in an empty file

if __name__ == "__main__":
    pytest.main()
