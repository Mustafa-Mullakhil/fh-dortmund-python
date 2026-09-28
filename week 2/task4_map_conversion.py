def string_to_list(s):
    return list(s)


strings = ["hello", "world", "python"]

result = list(map(string_to_list, strings))

print(f"Input:  {strings}")
print(f"Output: {result}")
