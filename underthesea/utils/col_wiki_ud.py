import os
from os import listdir
from os.path import join

from underthesea.file_utils import UNDERTHESEA_FOLDER
from underthesea.utils import logger
from underthesea.utils.col_script import UDDataset, UDSentence

WIKI_FOLDER = join(UNDERTHESEA_FOLDER, "data", "viwiki-20210720")
CLEANED_FOLDER = join(WIKI_FOLDER, "cleaned", "AA")
UD_FOLDER = join(WIKI_FOLDER, "ud", "AA")
os.makedirs(UD_FOLDER, exist_ok=True)


def check_line(line):
    return False if len(line) < 30 else not line.startswith("<")


def make_ud_file(file):
    logger.info(msg=file)
    sentences = []
    for i, line in enumerate(open(join(CLEANED_FOLDER, file)), start=1):
        s = UDSentence.load_from_raw_text(line)
        sentences.append(s)
        if i % 200 == 0:
            logger.info(f"{file}:{i}")
    ud_dataset = UDDataset(sentences)
    ud_dataset.write(join(UD_FOLDER, file))
    logger.info(f"Finish {file}")


if __name__ == '__main__':
    files = sorted(listdir(CLEANED_FOLDER))

    # with Pool(5) as p:
    #     p.map(make_ud_file, files)

    # file = files[0]
    # make_ud_file(file)

    for file in files:
        make_ud_file(file)
