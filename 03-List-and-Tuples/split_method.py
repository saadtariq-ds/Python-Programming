panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

panagram = """The quick brown 
fox jumps over 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7'
]
values = "".join(generated_list)
print(values)

values = values.split()
print(values)

# Converting to Integer: Approach 1
for index in range(len(values)):
    values[index] = int(values[index])

print(values)

# Converting to Integer: Approach 2
numerical_list = []
for value in values:
    numerical_list.append(int(value))

print(numerical_list)

