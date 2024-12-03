import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

# Writing to a file
with open(file='test_tuple.json', mode='w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

