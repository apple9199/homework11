def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = ""
    while n > 0:
        remainder = n % 2
        binary_digits = str(remainder) + binary_digits
        n = n // 2
        
    return binary_digits

# Take input from the user
decimal_num = int(input("Enter a decimal number: "))

# Convert and print the result
result = decimal_to_binary(decimal_num)
print(f"Binary: {result}")