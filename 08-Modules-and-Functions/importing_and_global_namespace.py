import fix_global_keyword
from fix_global_keyword import area_of_square

area = fix_global_keyword.area_of_square(40)
print(area)

# area = area_of_square(40)
# print(area)

print('Global namespace')
namespace = globals().copy()
for name, obj in namespace.items():
    print(name, obj)
