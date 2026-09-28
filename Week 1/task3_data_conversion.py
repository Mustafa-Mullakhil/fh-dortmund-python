print("=== Data Type Conversion ===\n")

num_int = 42
num_float = float(num_int)
print(f"1. Integer to Float: {num_int} -> {num_float}")
print(f"   Type: {type(num_float)}\n")

num_float2 = 3.14
num_int2 = int(num_float2)
print(f"2. Float to Integer: {num_float2} -> {num_int2}")
print(f"   Type: {type(num_int2)}\n")

num_int3 = 99
num_str = str(num_int3)
print(f"3. Integer to String: {num_int3} -> '{num_str}'")
print(f"   Type: {type(num_str)}\n")

str_num = "123"
int_from_str = int(str_num)
print(f"4. String to Integer: '{str_num}' -> {int_from_str}")
print(f"   Type: {type(int_from_str)}\n")

num_int4 = 1
bool_from_int = bool(num_int4)
print(f"5. Integer to Boolean: {num_int4} -> {bool_from_int}")
print(f"   Type: {type(bool_from_int)}")
