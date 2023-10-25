Sure, here's a `README.md` for the Modern Family script generator code:

---

# Modern Family Script Generator

The Modern Family Script Generator is a Python application that utilizes OpenAI's API to generate new episode scripts for Modern Family based on a given user prompt. It uses an existing pilot script to determine the character names and then requests the API to create a new script.

## Prerequisites

- Python 3.x
- OpenAI Python client. Install via pip:

```bash
pip install openai
```

- An API key from OpenAI. Ensure you have an active account with OpenAI and access to their GPT-3 API.

## Usage

1. Clone this repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Place your OpenAI API key in the `script.py`:

Replace the placeholder `openai.api_key = "YOUR_API_KEY_HERE"` with your actual API key.

3. Ensure the `pilot2.txt` file is in the same directory. This is the pilot script used for generation.

4. Run the script:

```bash
python script.py
```

5. Enter a basic plot or scenario for the new Modern Family episode when prompted.

6. The generated script will be saved to a file named `generated_script.txt`.

## Function Descriptions

- `extract_details_from_script(script_text)`: Extracts character names from a given script.
- `generate_script(pilot_script, user_prompt)`: Generates a new script based on the user's prompt and the provided pilot script.
- `read_script_from_file(filename)`: Reads a script from the given file.
- `save_script_to_file(script_content, filename="generated_script.txt")`: Saves the generated script to a specified file.

## Contributing

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

Save this to a file named `README.md` in the root directory of your project.
