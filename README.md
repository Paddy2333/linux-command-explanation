# Linux Command Explanation Tool

The Linux Command Explanation Tool is a web-based utility that uses OpenAI API to explain Linux commands in detail, helping beginners understand and learn how to use Linux commands.

## Installation

1. Clone the repository.
2. Install the required Python packages by running `pip install Flask` and `pip install openai`.
3. Set the OpenAI API key as an environment variable named `OPENAI_API_KEY`.
4. Run the Flask app by running `python main.py`.
5. Open your web browser and go to `http://localhost:5000`.

## Usage

1. Enter a Linux command in the input field.
2. Click the "Explain" button.
3. The tool will display a detailed explanation of the command.

## Credits

This project uses the OpenAI API and the text-davinci-003 model for command explanation. The front-end is styled with Tailwind CSS.
