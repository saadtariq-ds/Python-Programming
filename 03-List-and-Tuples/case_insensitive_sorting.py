pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ['Graham', 'John', 'terry', 'eric',
         'Terry', 'michael']
names.sort(key=str.casefold)
print(names)
