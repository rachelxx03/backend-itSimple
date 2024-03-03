from .api import actualSimplified
from .keyword_extraction import KeyphraseExtractionPipeline


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

            extractor = KeyphraseExtractionPipeline()
            return extractor(text)










