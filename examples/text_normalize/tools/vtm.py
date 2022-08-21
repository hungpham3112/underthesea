from .module import VietnameseTextNormalizer


def normalize(word):
    return VietnameseTextNormalizer.Normalize(word)
