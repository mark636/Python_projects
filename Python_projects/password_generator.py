import random

# Define letters and symbols
letters = ['a', 'b', 'c', 'd', 'e']
symbols = ['!', '@', '#', '$', '%']

# Combine letters, symbols, and numbers
characters = letters + symbols + [str(i) for i in range(10)]

# Function to generate a random password
def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))

# Specify password length
password_length = int(input("How many characters do you want your password to be?\n"))
password = generate_password(password_length)

print(f"Generated Password: {password}")
