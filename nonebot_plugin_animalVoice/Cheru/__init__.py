import re
from itertools import zip_longest

CHERU_SET = "切卟叮咧哔唎啪啰啵嘭噜噼巴拉蹦铃"
CHERU_DIC = {c: i for i, c in enumerate(CHERU_SET)}
ENCODING = "gb18030"
rex_split = re.compile(r"\b", re.U)
rex_word = re.compile(r"^\w+$", re.U)
rex_cheru_word: re.Pattern = re.compile(rf"切[{CHERU_SET}]+", re.U)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def word2cheru(w: str) -> str:
    c = ["切"]
    for b in w.encode(ENCODING):
        c.append(CHERU_SET[b & 0xF])
        c.append(CHERU_SET[(b >> 4) & 0xF])
    return "".join(c)


def cheru2word(c: str) -> str:
    if not c[0] == "切" or len(c) < 2:
        return c
    b = []
    for b1, b2 in grouper(c[1:], 2, "切"):
        x = CHERU_DIC.get(b2, 0)
        x = x << 4 | CHERU_DIC.get(b1, 0)
        b.append(x)
    return bytes(b).decode(ENCODING, "replace")


def str2cheru(s: str) -> str:
    c = []
    for w in rex_split.split(s):
        if rex_word.search(w):
            w = word2cheru(w)
        c.append(w)
    return "".join(c)


def cheru2str(c: str) -> str:
    return rex_cheru_word.sub(lambda w: cheru2word(w.group()), c)
