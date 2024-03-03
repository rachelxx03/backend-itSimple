from openai import OpenAI

from llm_retrival.call_llm.fleschk import calculate_flesch_reading_ease


def simplifiedText():
    client = OpenAI(api_key="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")
    # Define the prompt and additional text you want to enhance for readability
    prompt = "Enhance the readability of the following essay. Keep the core information and message intact but use simpler words and sentences:"
    additional_text = """Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer."""
    paragraph = 0
    # Make the API call with the corrected parameters
    response = client.chat.completions.create(
        model="gpt-4",  # Ensure you're using a valid model identifier
        messages=[
            {"role": "system", "content": additional_text},
            {"role": "user", "content": prompt}
        ]
        # The 'stream' parameter is optional and not needed for this use case
    )
    text_to_analyze = response.choices[0].message.content
    return text_to_analyze


def actualSimplified():
    product = simplifiedText()
    # Assuming you want to print the completion part by part
    results = {}
    count = 0
    score = calculate_flesch_reading_ease(product)
    while count < 5:
        if score < 80:
            results[score] = product
            product = simplifiedText()
        else:
            return product
        count += 1
    max_key = max(results.keys())
    return results[max_key]


a = actualSimplified()
print(a)