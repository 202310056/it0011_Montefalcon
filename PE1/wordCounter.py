exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

statement = input("Enter a string statement: ")

words = statement.split()

word_count = {}

for word in words:
    if word.lower() not in exclude_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

lowercase_words = []
uppercase_words = []

for word in word_count:
    if word.islower():
        lowercase_words.append((word, word_count[word]))
    else:
        uppercase_words.append((word, word_count[word]))

lowercase_words.sort()
uppercase_words.sort()

for word, count in lowercase_words:
    print(word.ljust(10), "-", count)

for word, count in uppercase_words:
    print(word.ljust(10), "-", count)

total_words = sum(word_count.values())
print("Total words filtered:", total_words)