import openai
import re

# Initialize OpenAI API
openai.api_key = "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"

def extract_details_from_script(script_text):
    characters = list(set(re.findall(r"(\w+):", script_text)))
    return characters

def generate_script(pilot_script, user_prompt):
    characters = extract_details_from_script(pilot_script)
    prompt_text = (f"{user_prompt}. Using characters {', '.join(characters)}, "
                   "please generate a Modern Family episode dialogue script:\n\n"
                   "----- START SCRIPT -----\n")
    
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      max_tokens=1000,
      temperature=0.7
    )
    
    script_content = response.choices[0].text.strip()
    # Only keep content after "START SCRIPT"
    script_content = script_content.split("----- START SCRIPT -----")[-1].strip()
    
    return script_content

def read_script_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def save_script_to_file(script_content, filename="generated_script.txt"):
    with open(filename, 'w') as file:
        file.write(script_content)
    print(f"Script saved to {filename}.")

# Read script from file
script_filename = "pilot2.txt"
pilot_script = read_script_from_file(script_filename)

# Take user input for a basic prompt
user_prompt = input("Enter a basic plot or scenario for the new Modern Family episode: ")

# Generate new script based on user prompt
new_script = generate_script(pilot_script, user_prompt)

# Save the generated script to a new file
save_script_to_file(new_script)
