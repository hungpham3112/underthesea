from elasticsearch import Elasticsearch
from apps.utils import DICTIONARY_FILE
import yaml

if __name__ == '__main__':
    with open(DICTIONARY_FILE) as f:
        content = f.read()

    es = Elasticsearch()

    words = yaml.safe_load(content)
    for i, (word_key, value) in enumerate(words.items(), start=1):
        data = {
            "headword": word_key,
            "senses": value
        }
        # es.index(index='dictionary', body=data, id=word_key)
        if i % 1000 == 0 and i > 0:
            print(i)
