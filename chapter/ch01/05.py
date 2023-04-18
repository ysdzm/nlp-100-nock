
_str = "I am an NLPer"

def ngram(list,n):
    gram = []
    for i in range(0,len(list)-n+1):
        gram.append(list[i:i+n])
    return gram

# 2文字ごとに取り出す
_char = [_str[idx:idx+1] for idx in range(0,len(_str))]
print(_char)
print(ngram(_char,2))

# 2単語ごと取り出す
_word = _str.split(" ")
print(_word)
print(ngram(_word,2))