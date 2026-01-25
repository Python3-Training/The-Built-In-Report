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
    with open(filename, 'r', encoding='utf-8') as f:
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
    return sorted(set(found_tokens))

if __name__ == "__main__":
    root = "3. Data model — Python 3.14.2 documentation"
    input_file  = root + ".txt"
    report_file = input_file + '.txt'
    tokens = find_tokens_starting_with_underscore(input_file)

    print(f"Found {len(tokens)} space-delimited '__' tokens:")
    with open(report_file, 'w') as fh:
        for ss, token in enumerate(tokens,1):
            print(f"{ss:03}.) {token}", file=fh)

