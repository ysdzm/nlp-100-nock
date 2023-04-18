
_str1 = "paraparaparadise"
_str2 = "paragraph"

X = set([_str1[idx:idx+2] for idx in range(0,len(_str1)-1)])
Y = set([_str2[idx:idx+2] for idx in range(0,len(_str2)-1)])

print("X")
print(X)
print("Y")
print(Y)

# 和集合
print("X | Y")
print(X | Y)
# 積集合
print("X & Y")
print(X & Y)
# 差集合
print("X - Y")
print(X - Y)
print("Y - X")
print(Y - X)
