import os

from dotenv import load_dotenv
from openai import OpenAI

from .fleschk import calculate_flesch_reading_ease

load_dotenv()
def simplifiedText(text):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("The OpenAI API key has not been set.")

    client = OpenAI(api_key=api_key)
    # Define the prompt and additional text you want to enhance for readability
    prompt = "Enhance the readability of the following essay. Keep the core information and message intact but use simpler words and sentences:"
    paragraph = 0
    # Make the API call with the corrected parameters
    response = client.chat.completions.create(
        model="gpt-4",  # Ensure you're using a valid model identifier
        messages=[
            {"role": "system", "content": text},
            {"role": "user", "content": prompt}
        ]
        # The 'stream' parameter is optional and not needed for this use case
    )
    text_to_analyze = response.choices[0].message.content
    return text_to_analyze


def actualSimplified(text):
    product = simplifiedText(text)
    # Assuming you want to print the completion part by part
    results = {}
    count = 0
    while count < 3:
        score = calculate_flesch_reading_ease(product)
        if score < 80:
            results[score] = product
            product = simplifiedText(text)
        else:
            return product
        count += 1
    max_key = max(results.keys())
    return results[max_key]


