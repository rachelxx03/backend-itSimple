def count_syllables(word):
    """Approximately count the syllables in a word."""
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


def calculate_flesch_reading_ease(text):
    """Calculate the Flesch Reading Ease score for a given text."""
    words = text.split()
    sentences = text.split('.')
    # Remove empty elements if any
    sentences = [s for s in sentences if s.strip()]

    # Counting syllables in the entire text
    syllables = sum(count_syllables(word) for word in words)

    # Calculating averages
    average_sentence_length = len(words) / len(sentences)
    average_syllables_per_word = syllables / len(words)

    # Applying the Flesch Reading Ease formula
    flesch_reading_ease_score = 206.835 - (1.015 * average_sentence_length) - (84.6 * average_syllables_per_word)

    return flesch_reading_ease_score

