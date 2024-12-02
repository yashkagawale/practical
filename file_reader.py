def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        num_lines = len(content)
        num_words = sum(len(line.split()) for line in content)
        return num_words, num_lines
    except FileNotFoundError:
        return "File not found!", 0

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    result = count_words_and_lines(file_path)
    if isinstance(result, tuple):
        print(f"Number of words: {result[0]}")
        print(f"Number of lines: {result[1]}")
    else:
        print(result)
