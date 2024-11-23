result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))
print(id(another_result))

print("---" * 30)

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ion"
print(id(result))
print(id(another_result))