text = input("Enter your text: ")

words = []
current_word = ""

for char in text:
    if char.isalpha():
        current_word += char
    elif char == "'" and current_word != "":
        current_word += char
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""

if current_word != "":
    words.append(current_word)

word_count = len(words)

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

total_length = 0

for word in words:
    total_length += len(word)

if word_count > 0:
    average_length = total_length / word_count
else:
    average_length = 0

print("Number of words:", word_count)
print("Longest word:", longest_word)
print("Longest word length:", len(longest_word))
print("Average word length:", round(average_length, 1))