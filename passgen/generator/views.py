import secrets
import string
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    def generate_secure_password(length, digits, letters, special_chars):
        """Generates a secure random password."""
        characters = ""
        if digits:
            characters += string.digits
        if letters:
            characters += string.ascii_letters
        if special_chars:
            characters += string.punctuation
        if not characters:
            raise ValueError("No character types selected for password generation.")

        return ''.join(secrets.choice(characters) for _ in range(length))


    def main():
        try:
                length = int(input("Enter the desired length of the password (min 8): "))
                if length < 8:
                    raise ValueError("Password length should be at least 8 characters.")
                digits = input("Include digits? (y/n): ").lower() == 'y'
                letters = input("Include letters? (y/n): ").lower() == 'y'
                special_chars = input("Include special characters? (y/n): ").lower() == 'y'
                password = generate_secure_password(length, digits, letters, special_chars)
                print("Generated Password:", password)
        except ValueError as e:
            print("Error generating password!", e)


            if __name__ == "__main__":
                main()

    return render(request, 'password.html', {'password': generate_secure_password})
