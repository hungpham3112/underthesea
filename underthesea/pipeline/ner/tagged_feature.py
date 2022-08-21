# ===========================
# token syntax
# ===========================
#         _ row 1
#        /  _ row 2
#       /  /  _ column
#      /  /  /
#    T[0,2][0]
#          .is_digit
#            \_ function
#
# ===========================
# sample tagged sentence
# ===========================
# this     A
# is       B
# a        C
# sample   D
# sentence E


import re
from underthesea.corpus import DictionaryLoader
words = DictionaryLoader("Viet74K.txt").words
lower_words = {word.lower() for word in words}


def text_lower(word):
    return word.lower()


def text_isdigit(word):
    return str(word.isdigit())


def text_isallcap(word):
    return all(letter.istitle() for letter in word)


def text_istitle(word):
    if len(word) == 0:
        return False
    try:
        titles = [s[0] for s in word.split(" ")]
        return all(token[0].istitle() is not False for token in titles)
    except Exception:
        return False


def text_is_in_dict(word):
    return str(word.lower() in lower_words)


def apply_function(name, word):
    functions = {
        "lower": text_lower,
        "istitle": text_istitle,
        "isallcap": text_isallcap,
        "isdigit": text_isdigit,
        "is_in_dict": text_is_in_dict
    }
    return functions[name](word)


def template2features(sent, i, token_syntax, debug=True):
    """
    :type token: object
    """
    columns = [[t[j] for t in sent] for j in range(len(sent[0]))]
    matched = re.match(
        "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?",
        token_syntax)
    column = matched["column"]
    column = int(column) if column else 0
    index1 = int(matched["index1"])
    index2 = matched["index2"]
    index2 = int(index2) if index2 else None
    func = matched["function"]
    prefix = f"{token_syntax}=" if debug else ""
    if i + index1 < 0:
        return [f"{prefix}BOS"]
    if i + index1 >= len(sent):
        return [f"{prefix}EOS"]
    if index2 is None:
        word = sent[i + index1][column]
    elif i + index2 >= len(sent):
        return [f"{prefix}EOS"]
    else:
        word = " ".join(columns[column][i + index1: i + index2 + 1])
    result = apply_function(func, word) if func is not None else word
    return [f"{prefix}{result}"]


def word2features(sent, i, template):
    features = []
    for token_syntax in template:
        features.extend(template2features(sent, i, token_syntax))
    return features
