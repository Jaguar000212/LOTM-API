'''
Helper functions for miscellaneous tasks
'''

from nltk import pos_tag

def format_name(text):
    
    ''' Format a name to be capitalized and separated by underscores '''
    
    tagged_words = pos_tag(text.split())

    # List of POS tags for words to be excluded
    excluded_pos_tags = ['IN', 'CC']
    
    capitalized_words = []
    for word, tag in tagged_words:
        if tag not in excluded_pos_tags:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())
    return '_'.join(capitalized_words)