import re

# converts text to lowercase
def to_lower(text):
    return text.lower()


# remove all the characters except alphabetical
# removes special characters and numerical charcharters
def remove_non_alpha(text):
    return re.sub(r'[^a-zA-Z]', ' ', text)

# Removes all blank lines
def remove_extra_blank_lines(content):   
    return re.sub(r'\n\s*\n', '\n', content)
    return txt

# splits stiong by space or " "
def split_string(text):
    return text.split()


# add space before and after the punctuation
def add_space_punc(text):
    return re.sub("([^a-zA-Z0-9])", r' \1 ', text)


# removes multiple spaces with single space
def remove_multi_space(text):
    return re.sub(r' +', ' ', text)


# removes all spaces 
# replaces " " with ""
def remove_all_space(text):
    return re.sub(r' +', '', text)

# check if substring present in text
def text_contains(text, substr):
    if(substr in text): 
        return 1
    else:
        return 0

# remove pattern from string
def strip_http_s(text, pattern_str):    
    return text.replace(pattern_str,"")


# extract sequence after last occurance
def extract_line_af(line, symbol_seq):
    return line.rsplit(symbol_seq)[-1]

# extract sequence after last occurance for multiple lines
def extract_line_af_all(content, symbol_seq):
    for line in content:
    	line_ex = extract_line_af(line, symbol_seq)
    	print(line_ex)


