vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-AM 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'starfighter': 'Lockhead F-104',
    'learjet': 'Bombardier Learjet 75',
    'toy': 'Glider',
}

print("Before Deleting")
for key, value in vehicles.items():
    print(key, value, sep=', ')

print()

print("After Deleting")
del vehicles['fiesta']

# Pop Method
# vehicles.pop('f1')
result = vehicles.pop('f1', None)
print(result)

plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)

for key, value in vehicles.items():
    print(key, value, sep=', ')
