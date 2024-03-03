from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('cmudict')
nltk.download('punkt')


# Assuming you've already downloaded cmudict using nltk.download('cmudict')
d = cmudict.dict()

def nsyl(word):
    # This function will return the number of syllables for the word
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

def count_sentences(text):
    sentences = sent_tokenize(text)
    return len(sentences)

def count_words(text):
    words = word_tokenize(text)
    return len(words)

def count_syllables(text):
    words = word_tokenize(text)
    syllable_count = sum(nsyl(word) for word in words if word.lower() in d)
    return syllable_count
def calculate_flesch_reading_ease(text):
    sentences = count_sentences(text)
    words = count_words(text)
    syllables = count_syllables(text)


    # Flesch Reading Ease formula
    try:
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    except ZeroDivisionError:
        score = 0
    return score


