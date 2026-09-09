
# Group Name: SYDN 02
# Group Members:4
# Aditya Banstola - S403120-
# Sandesh Regmi - S407215
# Aadesh Bhandari - S404328
# Sher Yuldashev - S406057


# Task 1: Character census
def character_census(text):
    #Return a dictionary with the five character counts for `text`.
    total_chars = 0
    letters = 0
    digits = 0
    whitespace = 0
    other = 0

    for char in text:
        # every character counts towards the total
        total_chars += 1

        if char.isalpha():# a-z, A-Z
            letters += 1
        elif char.isdigit():# 0-9
            digits += 1
        elif char.isspace(): # spaces, tabs, newlines
            whitespace += 1
        else:
            # anything left
            other += 1

    return {
        "total_chars": total_chars,
        "letters": letters,
        "digits": digits,
        "whitespace": whitespace,
        "other": other,
    }


def print_character_report(counts):
#Printing clearly labelled report for the character census
    print("----- Character Census -----")
    print(f"Total characters   : {counts['total_chars']}")
    print(f"Letters            : {counts['letters']}")
    print(f"Digits             : {counts['digits']}")
    print(f"Whitespace         : {counts['whitespace']}")
    print(f"Other characters   : {counts['other']}")

    # self-check: the four category counts should add up to the total
    check_sum = (
        counts["letters"]
        + counts["digits"]
        + counts["whitespace"]
        + counts["other"]
    )
    if check_sum == counts["total_chars"]:
        # counts line up so that nothing was missed or double-counted
        print(f"Self-check passed  : {check_sum} == {counts['total_chars']}")
    else:
        print(f"Self-check FAILED  : {check_sum} != {counts['total_chars']}")
    print()


def main():
    # hand it to the census function
    text = input("Enter a block of text to analyse:\n")
    counts = character_census(text)
    print_character_report(counts)


if __name__ == "__main__":
    main()