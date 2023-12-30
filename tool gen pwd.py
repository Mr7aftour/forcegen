import secrets
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length and character set
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Prompt the user for the desired password length
    password_length = int(input("Enter the desired password length: "))

    # Generate and print the password
    generated_password = generate_password(password_length)
    print("your passwordd:", generated_password)
