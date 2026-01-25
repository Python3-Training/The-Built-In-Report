# Generative: create a python program to list all of the
# space delimited '.__' tokens in a text file.
import re

def find_tokens_starting_with_underscore(filename):
    """
    Reads a text file, finds all space-delimited tokens starting with '__', 
    and returns them as a list.

    Args:
        filename (str): The name of the text file.

    Returns:
        list: A list of matching tokens.
    """
    found_tokens = []
    # Use 'with open()' to ensure the file is closed automatically
    with open(filename, 'r') as f:
        # Read the entire file content as a single string
        content = f.read()
        
        # The regular expression pattern explanation:
        # \\b ensures the match is a whole word boundary.
        # __ matches the literal characters "__".
        # \\w* matches zero or more word characters (alphanumeric and underscore) after "__".
        # This matches tokens like "__init__", "__main", "__some_var" when space delimited.
        pattern = r"\b__\w*\b"
        
        # Use re.findall to find all occurrences of the pattern in the content
        found_tokens = re.findall(pattern, content)
        
    # Return a set of tokens to ensure uniqueness, then convert back to a list
    # to list all occurrences, keep as list; if only unique tokens are needed, 
    # use set(found_tokens)
    return found_tokens

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create a dummy text file for testing
    dummy_filename = "sample_text.txt"
    with open(dummy_filename, "w") as f:
        f.write("This is a sample text file.\n")
        f.write("It contains some tokens like __init__, __main, and __some_variable.\n")
        f.write("It also includes things like __not a match as it is not space delimited__.\n")
        f.write("Also, __another_token__ and end of line __endline_token\n")

    # 2. Run the function
    tokens = find_tokens_starting_with_underscore(dummy_filename)

    # 3. Print the results
    print(f"Found {len(tokens)} space-delimited '__' tokens:")
    for token in tokens:
        print(f"- {token}")
    
    # Optional: remove the dummy file
    # import os
    # os.remove(dummy_filename)
