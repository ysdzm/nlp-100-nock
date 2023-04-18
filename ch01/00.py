_str = "stressed"

print(_str)

# リストに入れて取り出す
_list = []
for c in _str:
    _list.append(c)
_reverse = ""
while len(_list):
    _reverse += _list.pop()
print(_reverse)

# 後ろから順に取り出した文字列
print(_str[::-1])

# 逆転して文字列に結合
print(''.join(list(reversed(_str))))