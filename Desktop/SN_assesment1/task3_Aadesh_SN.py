# Task 3: Word statistics

def word_statistics(text):
    #Return total word count, longest word, and average word length
    total_words = 0
    longest_word = ""
    longest_length = 0
    total_length = 0
    current_word = ""

    for char in text:
        if char.isalpha() or char == "'":
    # letters and apostrophes build up the current word
            current_word += char
        else:
     # anything else ends a word
            if current_word != "":
                total_words += 1
                total_length += len(current_word)
                if len(current_word) > longest_length:
                    # first word to reach this length wins ties,
                    longest_word = current_word
                    longest_length = len(current_word)
                current_word = ""

    # check for a trailing word
    if current_word != "":
        total_words += 1
        total_length += len(current_word)
        if len(current_word) > longest_length:
            longest_word = current_word
            longest_length = len(current_word)

    if total_words > 0:
        average_length = round(total_length / total_words, 1)
    else:
        average_length = 0

    return {
        "total_words": total_words,
        "longest_word": longest_word,
        "longest_length": longest_length,
        "average_length": average_length,
    }


def print_word_report(stats):
    #Print a clearly labelled report for the word statistics
    print("----- Word Statistics -----")
    print(f"Total words        : {stats['total_words']}")
    print(f"Longest word       : '{stats['longest_word']}' ({stats['longest_length']} letters)")
    print(f"Average word length: {stats['average_length']}")
    print()


def get_multiline_input():
#Read text over several lines, stopping at a blank line
    print("Enter your text below. Press Enter on an empty line when done:")
    text = ""
    while True:
        line = input()
        if line == "":
            # empty line signals the end of input
            break
        if text != "":
            # add the newline back in between lines
            text += "\n"
        text += line
    return text


def main():
    text = get_multiline_input()
    stats = word_statistics(text)
    print_word_report(stats)


if __name__ == "__main__":
    main()
