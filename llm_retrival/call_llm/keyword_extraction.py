from transformers import (
    TokenClassificationPipeline,
    AutoModelForTokenClassification,
    AutoTokenizer,
)
from transformers.pipelines import AggregationStrategy
import numpy as np

# Define keyphrase extraction pipeline
class KeyphraseExtractionPipeline(TokenClassificationPipeline):
    def __init__(self, model = "ml6team/keyphrase-extraction-kbir-inspec", *args, **kwargs):
        super().__init__(
            model=AutoModelForTokenClassification.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )

    def postprocess(self, model_outputs, aggregation_strategy=AggregationStrategy.SIMPLE, **kwargs):
        # Call the superclass's postprocess with the correct parameters
        results = super().postprocess(
            model_outputs=model_outputs,
            aggregation_strategy=aggregation_strategy,
            **kwargs
        )
        # Process results to extract unique keyphrases
        unique_keyphrases = np.unique([result.get("word").strip() for result in results])
        return unique_keyphrases





extractor = KeyphraseExtractionPipeline()

# Inference
text = """
Keyphrase extraction is a technique in text analysis where you extract the
important keyphrases from a document. Thanks to these keyphrases humans can
understand the content of a text very quickly and easily without reading it
completely. Keyphrase extraction was first done primarily by human annotators,
who read the text in detail and then wrote down the most important keyphrases.
The disadvantage is that if you work with a lot of documents, this process
can take a lot of time. 
Here is where Artificial Intelligence comes in. Currently, classical machine
learning methods, that use statistical and linguistic features, are widely used
for the extraction process. Now with deep learning, it is possible to capture
the semantic meaning of a text even better than these classical methods.
Classical methods look at the frequency, occurrence and order of words
in the text, whereas these neural approaches can capture long-term
semantic dependencies and context of words in a text.
""".replace("\n", " ")

keyphrases = extractor(text)

print(keyphrases)
