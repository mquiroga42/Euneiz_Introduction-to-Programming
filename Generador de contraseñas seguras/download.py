"""
Download a list of words to a text file.
"""

def download_dictionary(word_list, file_name):
    """
    Download a list of words to a text file.
    Args:
    word_list (list): The list of words to be written to the file.
    file_name (str): The name of the destination file.
    Returns:
    None
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            for word in word_list:
                file.write(word + '\n')
        print(f"List saved to {file_name}")
    except IOError:
        print("Error writing the file.")
