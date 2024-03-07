from .api import actualSimplified
from .keyword_extraction import KeyphraseExtractionPipeline
import string


class Controller():

        def __init__(self, text ):
               self.text = text

        def get_text(self):
            return self.text

        def set_text(self,text):
            self.text = text
        def get_paraphrase(self,text):
            return actualSimplified(text)

        def get_key_word(self,text):

            extractor = KeyphraseExtractionPipeline(model="ml6team/keyphrase-extraction-kbir-openkp")
            punctuation = string.punctuation
            trans_table = str.maketrans('', '', punctuation)
            cleaned_words = [word.translate(trans_table) for word in extractor(text)]
            return cleaned_words










