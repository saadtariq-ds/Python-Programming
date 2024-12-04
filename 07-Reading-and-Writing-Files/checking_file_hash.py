import hashlib

published_hash = "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"

filename = 'colorama-0.4.6-py2.py3-none-any.whl'

with open(file=filename, mode='rb') as downloaded_file:
    contents = downloaded_file.read()

file_hash = hashlib.sha256(contents).hexdigest()
print(file_hash)

if file_hash != published_hash:
    print(f"The file {filename} has been modified")
else:
    print(f"The file {filename} hash is correct")