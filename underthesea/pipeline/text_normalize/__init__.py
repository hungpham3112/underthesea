from .token_normalize import token_normalize
from underthesea.pipeline.word_tokenize.regex_tokenize import tokenize


def text_normalize(text, tokenizer='underthesea'):
    """

    Args:
        tokenizer (str): space or underthesea
    """
    tokens = tokenize(text) if tokenizer == 'underthesea' else text.split(" ")
    normalized_tokens = [token_normalize(token) for token in tokens]
    return " ".join(normalized_tokens)
