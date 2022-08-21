from os.path import dirname, join
import joblib
import logging
from data import Dictionary, Word

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s')


CORPUS_FOLDER = dirname(dirname(__file__))
DICT_FOLDER = join(CORPUS_FOLDER, "data", "underthesea_v170")
UTS_DICT_DATA = join(DICT_FOLDER, "underthesea_dictionary.data")

KNOWN_POS = {
    'V': 'VERB',
    'N': 'NOUN',
    'A': 'ADJ',
    'P': 'PROPN',
    'C': 'CCONJ',
    'I': 'INTJ',
    'E': 'ADP',
    'M': 'NOUN',  # số từ
    'n': 'NOUN',
    'S': 'NOUN'  # khối
}
TEMP_IGNORE_POS = {'R', 'X', 'Z', 'D', 'O'}
logger.info("Start loading")
dict = Dictionary()
pos_count = {}
data = joblib.load(UTS_DICT_DATA)
count = 0
logger.info("End loading")

for key in data:
    # count += 1
    # if count > 30:
    #     break
    defs = []
    pos_tags = {}
    text = key
    for definition in data[text]:
        pos_tag = definition['pos']
        if pos_tag not in pos_tags:
            i = len(pos_tags)
            pos_tags[pos_tag] = i
            tag_data = {'tag': pos_tag, 'defs': []}
            defs.append(tag_data)
        index = pos_tags[pos_tag]
        defs[index]["defs"].append({
            "def": definition['definition'],
            'examples': [
                definition['example']
            ]
        })
    word = Word(text, defs)
    dict.add(word)
logger.info("End Process")
dict.save(join(DICT_FOLDER, 'underthesea_dictionary.yaml'))
logger.info("End Save")
print('[+] Done')
