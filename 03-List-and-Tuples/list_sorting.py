even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(f"Even List: {even}")
print(f"Odd List: {odd}")

even.extend(odd)
print(f"Even List after Extend: {even}")

even.sort()
print(f"Even List after Sort: {even}")

even.sort(reverse=True)
print(f"Even List after Sorting in Reverse Order: {even}")
