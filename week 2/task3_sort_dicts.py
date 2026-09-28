original_list = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

print("Original list of dictionaries:")
for item in original_list:
    print(f"  {item}")

sorted_list = sorted(original_list, key=lambda x: x['model'])

print("\nSorted list of dictionaries (by model):")
for item in sorted_list:
    print(f"  {item}")
