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







