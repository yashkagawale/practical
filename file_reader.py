def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return "File not found!"

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    result = count_words(file_path)
    print(f"Number of words: {result}")

