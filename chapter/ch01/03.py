import re

_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# , と . を置換して、残りを空白で分割
_split = re.split('\s',_str.translate(str.maketrans({".":"",",":""})))

_splitLen = []

for i in range (0, len(_split)):
    # 各長さを記録
    _splitLen.insert(i,len(_split[i]))

print(_splitLen)