def sum_and_average_of_digits(s1):
    digits = [int(char) for char in s1 if char.isdigit()]

    if len(digits) == 0:
        return 0, 0

    total_sum = sum(digits)
    average = total_sum / len(digits)

    return total_sum, average


test_string = input("Enter a string with digits: ")

total_sum, average = sum_and_average_of_digits(test_string)

print(f"\nString: '{test_string}'")
print(f"Sum of digits: {total_sum}")
print(f"Average of digits: {average:.2f}")
