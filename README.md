# Professional Email Generator

## Overview
This Python script utilizes the langchain library and OpenAI's language model to generate professional email content. 
It prompts the user to input email content, client name, and sender name, then generates an email with optimized content 
and a customized signature, using an AI language model.

## Installation
Before running the script, ensure you have installed the following dependencies:
- langchain library: `pip install langchain`
- OpenAI library: `pip install openai` deprecated, now use `pip install -U langchain-openai`

### API Key Setup
To use the OpenAI language model in the script, you need to obtain an API key from OpenAI. Follow these steps:
1. Sign up for an account on the [OpenAI website](https://openai.com/).
2. Generate an API key from your account dashboard.
3. Replace the `openai_api_key` variable in the script with your API key.

## Usage
1. Run the script.
2. Input the email content, client name, and sender name when prompted.
3. The script will generate a professional email based on the provided inputs.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have any suggestions, improvements, or bug fixes.

## License
This project is licensed under the [MIT License](LICENSE).