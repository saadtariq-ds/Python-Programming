# equations = bytes((207, 128, 114, 194, 178))
equations = b'\xcf\x80r\xc2\xb2'

print(equations)
print(type(equations))
print(len(equations))

for b in equations:
    print(b, end=', ')
print()
