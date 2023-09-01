import string

def replace_words(input_text):
    # Split the input text into words, keeping punctuation attached to words
    words = []
    current_word = ""
    for char in input_text:
        if char.isalnum() or char == "'":
            current_word += char
        else:
            if current_word:
                words.append(current_word)
            current_word = ""
            words.append(char)
    if current_word:
        words.append(current_word)

    count = words.count("terrible")
    replaced_count = 0

    for i in range(len(words)):
        if words[i] == "terrible":
            if replaced_count % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"

            replaced_count += 1

    output_text = ''.join(words)
    return count, output_text

def main():
    # Read the file
    with open("file_to_read.txt", "r") as file:
        input_text = file.read()

    count, output_text = replace_words(input_text)

    # Write to a new file
    with open("result.txt", "w") as file:
        file.write(output_text)

    print(f"The word 'terrible' appears {count} times.")

if __name__ == "__main__":
    main()