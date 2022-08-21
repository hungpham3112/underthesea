# -*- coding: utf-8 -*-
from .regex_tokenize import tokenize
from .model import CRFModel


def word_tokenize(sentence, format=None, use_token_normalize=True):
    """
    Vietnamese word segmentation

    Parameters
    ==========

    sentence: {unicode, str}
        raw sentence

    Returns
    =======
    tokens: list of text
        tagged sentence

    Examples
    --------

    >>> # -*- coding: utf-8 -*-
    >>> from underthesea import word_tokenize
    >>> sentence = "Bác sĩ bây giờ có thể thản nhiên báo tin bệnh nhân bị ung thư"

    >>> word_tokenize(sentence)
    ['Bác sĩ', 'bây giờ', 'có thể', 'thản nhiên', 'báo tin', 'bệnh nhân', 'bị', 'ung thư']

    >>> word_tokenize(sentence, format="text")
    'Bác_sĩ bây_giờ có_thể thản_nhiên báo_tin bệnh_nhân bị ung_thư'
    """
    tokens = tokenize(sentence, use_token_normalize=use_token_normalize)
    crf_model = CRFModel.instance()
    output = crf_model.predict(tokens, format)
    tokens = [token[0] for token in output]
    tags = [token[1] for token in output]
    output = []
    for num_words, (tag, token) in enumerate(zip(tags, tokens)):
        if tag == "I-W" and num_words > 0:
            output[-1] = f"{output[-1]} {token}"
        else:
            output.append(token)
    if format == "text":
        output = u" ".join([item.replace(" ", "_") for item in output])
    return output
