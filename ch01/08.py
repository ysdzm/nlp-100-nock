
_text = input()

def cipher(_text):
    _ans = ""
    for i in range(0,len(_text)):
        if(_text[i].islower()):
            # chr() と ord() を使おう
            _ans += chr(219-ord(_text[i]))
        else:
            _ans += _text[i]
    return _ans

print(cipher(_text))            # 暗号化
print(cipher(cipher(_text)))    # 復号

