"""Helper functions for miscellaneous tasks"""

from nltk import pos_tag


def format_name(text):
    """
    This function takes a string as input, splits it into words, and capitalizes each word that is not a preposition or conjunction.
    It then joins the words together with underscores and returns the result.

    Parameters:
    text (str): The input string to be formatted.

    Returns:
    str: The formatted string with capitalized words (excluding prepositions and conjunctions) joined by underscores.
    """
    # POS tagging the words in the input string
    tagged_words = pos_tag(text.split())

    # List of POS tags for words to be excluded
    excluded_pos_tags = ["IN", "CC"]

    # Capitalizing each word that is not a preposition or conjunction
    capitalized_words = []
    for word, tag in tagged_words:
        if tag not in excluded_pos_tags:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())

    return "_".join(capitalized_words)
