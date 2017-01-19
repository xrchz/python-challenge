def char_range(c1,c2):
    return ''.join(map(chr,range(ord(c1),ord(c2)+1)))

trans1 = char_range('a','z')
trans2 = char_range('c','z') + 'ab'
trans = str.maketrans(trans1,trans2)
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
print(s.translate(trans))
print("map".translate(trans))
