
import re

_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# , と . を置換して、空白区切りで分割
_split = re.split('\s',_str.translate(str.maketrans({".":"",",":""})))

print(_split)

_nums = [1,5,6,7,8,9,15,16,19]

# 該当するとき、指定された出力方法で出力
for i in range(0,len(_split)):
    if i+1 in _nums:
        print(_split[i][0:1:])
    else:
        print(_split[i][0:2:])