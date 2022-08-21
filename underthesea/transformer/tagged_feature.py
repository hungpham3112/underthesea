from os.path import join, dirname
from underthesea.reader.dictionary_loader import DictionaryLoader

words = DictionaryLoader(join(dirname(__file__), "Viet74K.txt")).words
lower_words = {word.lower() for word in words}


def text_lower(word):
    return word.lower()


def text_isdigit(word):
    return word.isdigit()


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


functions = {
    "lower": text_lower,
    "istitle": text_istitle,
    "isallcap": text_isallcap,
    "isdigit": text_isdigit,
    "is_in_dict": text_is_in_dict
}
