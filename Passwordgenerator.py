# Generate a passwords.txt file with numeric passwords

filename = "passwords.txt"
max_length = 6  # Max length of passwords

with open(filename, "w") as f:
    # Add sequential numbers
    for i in range(1, 10**max_length):
        f.write(str(i).zfill(max_length) + "\n")
    
    # Add repeated patterns (e.g., 1111, 2222, etc.)
    for digit in range(10):
        pattern = str(digit) * max_length
        f.write(pattern + "\n")
    
    # Add random variations (examples)
    f.write("123456\n")
    f.write("654321\n")
    f.write("314159\n")  # Pi-like sequence

print(f"'{filename}' created with passwords!")
