a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking Tuple")
data = 1, 2, 76     # represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a List")
my_list = [12, 13, 14]
p, q, r = my_list
print(p)
print(q)
print(r)
print()

for t in enumerate("abcdefgh"):
    # print(t)
    index, character = t
    print(index, character)