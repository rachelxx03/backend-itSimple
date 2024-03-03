from openai import OpenAI
def simplifiedText():
    client = OpenAI(api_key="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")
    # Define the prompt and additional text you want to enhance for readability
    prompt = "Strictly improve the Flesch-Kincaid Reading Ease to always above 80"
    additional_text = "Whenever how well you do depends on how well you've done, you'll get exponential growth. But neither our DNA nor our customs prepare us for it. No one finds exponential growth natural; every child is surprised, the first time they hear it, by the story of the man who asks the king for a single grain of rice the first day and double the amount each successive day."
    paragraph = 0
    # Make the API call with the corrected parameters
    response = client.chat.completions.create(
        model="gpt-4",  # Ensure you're using a valid model identifier
        messages=[
            {"role": "user", "content": additional_text},
            {"role": "system", "content": prompt }
        ]
        # The 'stream' parameter is optional and not needed for this use case
    )

    # Assuming you want to print the completion part by part
    for choice in response.choices:
        return choice.message.content
a = simplifiedText()
print(a)
