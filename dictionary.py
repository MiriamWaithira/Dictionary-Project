import json
from difflib import get_close_matches

# Load the JSON dictionary data
def load_dictionary(file_path):
    with open(file_path) as f:
        return json.load(f)


# Define the function to get definitions or suggest words
def get_definition(word, dictionary_data):
    # Normalize to lowercase to handle case variations
    word = word.lower()

    # Direct match
    if word in dictionary_data:
        definitions = dictionary_data[word]
        # If multiple definitions, join them with a newline
        if isinstance(definitions, list):
            return "\n".join(definitions)
        else:
            return definitions # For a single definition, return as is
    
    # Handle misspellings by suggesting similar words
    close_matches = get_close_matches(word, dictionary_data.keys(), n=1, cutoff=0.8)
    if close_matches:
        definitions = dictionary_data[close_matches[0]]
        if isinstance(definitions, list):
            return f"Did you mean '{close_matches[0]}'? Definition:\n" + "\n".join(definitions)
        else:
            return f"Did you mean '{close_matches[0]}'? Definition: {definitions}"
    else:
        return "Word not found. Please check the spelling nad try again."

# Main program
if __name__ == "__main__":
    # Load the dictionary data
    dictionary_data = load_dictionary('dictionarydata.json')

    # Prompt the user for a word
    while True:
        word = input("Enter a word to search its definition (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the dictionary. Goodbye!")
            break
        # Display the definition or suggestion
        print(get_definition(word, dictionary_data))