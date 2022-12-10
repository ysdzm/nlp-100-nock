
import re
import random

_text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(_text)

# , を置換し、空白区切りで分割
_word = re.sub("\s+"," ",_text.translate(str.maketrans({",":""}))).split(" ")

for i in range(0,len(_word)):
    if(len(_word[i]) >= 4):
        _list = list(_word[i][1:-1])
        random.shuffle(_list)           # シャッフル
        _word[i] = _word[i][0] + "".join(_list) + _word[i][-1]

print(" ".join(_word))