def commonSubstring(a, b):
    return 'YES' if any(i in b for i in a ) else 'NO'

print(commonSubstring(["hello","hi"], ["world", "bye"]))