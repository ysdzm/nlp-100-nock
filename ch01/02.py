_str1 = "パトカー"
_str2 = "タクシー"

_str = ""

# 2つとも長さ4なので、4回要素を取り出していく
for i in range(4):
    _str += _str1[i]
    _str += _str2[i]

print(_str)