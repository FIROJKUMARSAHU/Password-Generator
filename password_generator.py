import random as rnd
import string as str

def generate_pwd(length, use_letters, use_numbers, use_symbols):
    characters = ""
    
    if use_letters:
        characters += str.ascii_letters
    if use_numbers:
        characters += str.digits
    if use_symbols:
        characters += str.punctuation

    if not characters:
        print("Error: No character types selected. Please enable at least one option.")
        return None

    password = ''.join(rnd.choice(characters) for _ in range(length))
    return password

def get_bool_input(pro):
    while True:
        res = input(pro + " (y/n): ").strip().lower()
        if res == 'y':
            return True
        elif res == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def mainfun():
    print("=== Password Generator ===")
    print("-"*50)

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Length must be a positive integer.")
            return

        use_letters = get_bool_input("Include letters")
        use_numbers = get_bool_input("Include numbers")
        use_symbols = get_bool_input("Include symbols")

        password = generate_pwd(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")

if __name__ == "__main__":
    mainfun()