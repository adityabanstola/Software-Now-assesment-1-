# Task 4: Line and sentence analysis

def line_sentence_analysis(text):
    # Return the number of lines, sentences, and the longest line length
    num_lines = 1  # start at 1 since the last line has no trailing newline
    num_sentences = 0
    longest_line_length = 0
    current_line_length = 0

    for char in text:
        if char == "\n":
            # newline marks the end of a line, so start a new count
            num_lines += 1

            if current_line_length > longest_line_length:
                longest_line_length = current_line_length

            current_line_length = 0

        else:
            current_line_length += 1

            if char in ".!?":
                # each of these characters marks the end of a sentence
                num_sentences += 1

    # Check the final line
    if current_line_length > longest_line_length:
        longest_line_length = current_line_length

    return {
        "num_lines": num_lines,
        "num_sentences": num_sentences,
        "longest_line_length": longest_line_length,
    }


def print_line_sentence_report(stats):
    # Print a clearly labelled report
    print("----- Line and Sentence Analysis -----")
    print(f"Number of lines    : {stats['num_lines']}")
    print(f"Number of sentences: {stats['num_sentences']}")
    print(f"Longest line length: {stats['longest_line_length']}")
    print()


def get_multiline_input():
    # Read text over several lines, stopping at a blank line
    print("Enter your text below. Press Enter on an empty line when done:")

    text = ""

    while True:
        line = input()

        if line == "":
            # Empty line signals the end of input
            break

        if text != "":
            # Add the newline back in between lines
            text += "\n"

        text += line

    return text


def main():
    # Building full block of text from multiple lines of input
    text = get_multiline_input()
    stats = line_sentence_analysis(text)
    print_line_sentence_report(stats)


if __name__ == "__main__":
    main()