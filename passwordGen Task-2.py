import random
import string

def generate_password(length=12, use_special_chars=True):
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""

    all_chars = lower_chars + upper_chars + digits + special_chars

    if not all_chars:
        raise ValueError("No characters available to generate the password.")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    generated_password = generate_password(length=password_length, use_special_chars=include_special_chars)
    print("Generated Password:", generated_password)
