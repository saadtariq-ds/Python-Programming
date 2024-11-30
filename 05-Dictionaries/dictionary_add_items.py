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

print("Before Adding Items")
for key, value in vehicles.items():
    print(key, value, sep=', ')

vehicles["starfighter"] = "Lockhead F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

print()

print("After Adding Items")
for key, value in vehicles.items():
    print(key, value, sep=', ')
