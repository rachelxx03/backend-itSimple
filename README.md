# Backend-itSimple

## Getting Started

Before you can run the backend, you need to set up an OpenAI API key. This key allows access to client.chat.completions.create() call to model gpt-4 that simplifies the content.

### Prerequisites

- An OpenAI account. If you don't have one, you can create an account at [https://openai.com](https://openai.com).
- Python 3.9 or higher.

### Setting Up Your OpenAI API Key

1. **Obtain an API Key:**
   - Log in to your OpenAI account.
   - Navigate to the API section and generate a new API key.

2. **Configure the API Key in Your Local Environment:**
   - This project uses environment variables to manage sensitive information. To set up your OpenAI API key, create a file named `.env` in the root directory of the project and add the following line:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with the API key you obtained from OpenAI.

3. **Install Dependencies:**
   - Run the following command to install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

### Running the Project

- After setting up your API key and installing the dependencies, you can run the project by executing:
  ```bash
  python manage.py runserver
  ```

## Security Notice

Please ensure that your `.env` file is never committed to version control to keep your OpenAI API key secure. This project's `.gitignore` file is configured to exclude `.env`, but always double-check before committing new files.

## Troubleshooting

- If you encounter a `ValueError: The OpenAI API key has not been set.` error, please ensure that your `.env` file is correctly set up and located in the project's root directory, and that you've restarted your development environment after making changes to environment variables.

---


SPECIFICS

Keystroke Extraction Model Used: [distilbert-kptimes](https://huggingface.co/ml6team/keyphrase-extraction-distilbert-kptimes)



