# Dictionary-Project
This is a python project to create a program that checks the meaning of words. The dictionary data is from a json file.
This program provides definitions for words from a JSON-based dictionary.

The KEY FEATURES:

1. Loading Dictionary Data: The 'load_dictionary' function loads word definitions from a JSON file into a Python dictionary for fast lookups.

2. Definition Lookup: The 'get_definition' function takes a word and searches for its definition in a case-insensitive manner. If the word has multiple definitions, they are displayed on separate lines.

3. Spell Check and Suggestions: If an exact match is not found, the program uses Python's 'difflib' to suggest the closest matching word. The user is presented with the suggested word and its definition if available.

4. Interactive User Interface: In the main program, users are prompted to enter words and receive definitions or suggestions until they type 'exit' to quit the program.

HAPPY CODING!!!