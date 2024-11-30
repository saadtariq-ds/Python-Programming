vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-AM 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

print("Before Changing")
for key, value in vehicles.items():
    print(key, value, sep=', ')

print()
print("After Changing Value of virago")

vehicles['virago'] = "Yamaha XV535"

for key, value in vehicles.items():
    print(key, value, sep=', ')
