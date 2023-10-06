import sys

def main():
    file_path = input("File name: ")
    WordFrequencyCounter(file_path)
    print(f"Word count: {word_count}")

def WordFrequencyCounter(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            words = file_content.split()
            return len(words)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()