# Function to count syllables in a word (basic approximation)
def count_syllables(word):
    word = word.lower()
    syllables = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllables += 1
    if word.endswith("e"):
        syllables -= 1
    if syllables == 0:
        syllables = 1
    return syllables

# Text to analyze
text = "When something you do gets better the more you do it, things can grow really fast. But we're not naturally ready for this. Even our traditions don't help. It's a strange idea for everyone. Take the story of a man who asked a king for just one grain of rice and then double that every day. It surprises kids every time they hear it."

# Splitting the text into words and sentences
words = text.split()
sentences = text.split('.')
# Remove empty elements if any
sentences = [s for s in sentences if s]

# Counting syllables in the entire text
syllables = sum(count_syllables(word) for word in words)

# Calculating averages
average_sentence_length = len(words) / len(sentences)
average_syllables_per_word = syllables / len(words)

# Applying the Flesch Reading Ease formula
flesch_reading_ease_score = 206.835 - (1.015 * average_sentence_length) - (84.6 * average_syllables_per_word)

print(f"Flesch Reading Ease Score: {flesch_reading_ease_score}")
