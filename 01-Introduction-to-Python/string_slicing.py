parrot = "Norwegian Blue"
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(parrot[0:5])
print(parrot[3:5])
print(parrot[4:])
print(parrot[:5])
print(parrot[10:])
print("--" * 25)

# Negative Slicing
print(parrot[-4:-2])
print(parrot[-4:12])
print('--' * 25)

# Step Value in Slicing
print(parrot[0:6:2])
print(parrot[0:6:3])
print(parrot[0::3])
print('--' * 25)

# Slicing Backwards
print(parrot[13:9:-1])
print('--' * 25)

# Challenge
print(alphabet[16:13:-1])   #qpo
print(alphabet[4::-1])   #edcba
print(alphabet[25:17:-1])   #last 8 characters, in reverse order
