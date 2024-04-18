names="balaji srinivasan"
vowel="aeiou"
res=[char for char in names if char in vowel]
print(res)
ress=[char for char in names if char not in vowel]
print(ress)
print(names[::-1])
print(names[1:17:3])
for i in names:
    print(i,end='-')
    