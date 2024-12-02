filename = "Jabberwocky.txt"
with open(file=filename, mode='r') as poem:
    first = poem.readline().rstrip()

print(first)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)

toves_removed = first.removesuffix("toves")
print(toves_removed)


def remove_prefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def remove_suffix(string:str, suffix:str) -> str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


print()
twas_removed = remove_prefix(first, "'Twas")
print(twas_removed)

toves_removed = remove_suffix(first, "toves")
print(toves_removed)
