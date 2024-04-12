def count_words_in_file(path):
    try:
        with open(path, 'r') as file:
            file_content = file.read()
            return f"data = {file_content.split()}\nlength of the words: {len(file_content.split())}"
    except FileNotFoundError:
        return "Please provide a valid file path."

file_path = "example.txt"
print(count_words_in_file(file_path))
