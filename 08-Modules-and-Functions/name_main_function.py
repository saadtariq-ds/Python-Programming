""" Module for investigating importing and namespace """
import main_fix_global_keyword
from main_fix_global_keyword import area_of_square

area = main_fix_global_keyword.area_of_square(40)
area = area_of_square(40)
print(area)


print('Global namespace')
namespace = globals().copy()
for name, obj in namespace.items():
    print(name, obj)
