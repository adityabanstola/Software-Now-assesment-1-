# Task 2: Case and vowel breakdown

def case_vowel_breakdown(text):
    #Return a dictionary with case, vowel/consonant, and per-vowel counts
    upper = 0
    lower = 0
    vowels = 0
    consonants = 0
    vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for char in text:
        if not char.isalpha():
            # skip anything that isn't a letter
            continue

        if char.isupper():
            upper += 1
        else:
            lower += 1

        lower_char = char.lower()
        if lower_char in "aeiou":
            # counts as a vowel regardless of original case
            vowels += 1
            vowel_counts[lower_char] += 1
        else:
            consonants += 1

    return {
        "upper": upper,
        "lower": lower,
        "vowels": vowels,
        "consonants": consonants,
        "vowel_counts": vowel_counts,
    }


def print_case_vowel_report(counts):
    #Print a clearly labelled report for the case/vowel breakdown
    print("----- Case and Vowel Breakdown -----")
    print(f"Uppercase letters  : {counts['upper']}")
    print(f"Lowercase letters  : {counts['lower']}")
    print(f"Vowels             : {counts['vowels']}")
    print(f"Consonants         : {counts['consonants']}")

    # print each vowel's individual count
    for vowel in "aeiou":
        print(f"  '{vowel}' count       : {counts['vowel_counts'][vowel]}")
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
            # adding newline back in between lines
            text += "\n"
        text += line
    return text


def main():
    text = get_multiline_input()
    counts = case_vowel_breakdown(text)
    print_case_vowel_report(counts)


if __name__ == "__main__":
    main()