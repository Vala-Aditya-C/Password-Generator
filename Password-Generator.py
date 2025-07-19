import random
import string
def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4 characters."
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))

    return password
if __name__ == "__main__":
    try:
        user_length = int(input("Enter the desired password length (minimum 4): "))
        print("Generated Password:", generate_password(user_length))
    except ValueError:
        print("Please enter a valid integer for the password length.")
