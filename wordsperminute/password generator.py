import random
import string

def generate_password():
    print("--- Secure Password Generator ---")
    
    # 1. Error Catch for input collection
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            # Manually trigger an error if the user enters a negative number or zero
            raise ValueError("Password length must be greater than 0.")
            
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include special symbols? (y/n): ").strip().lower() == 'y'
        
        # Check if the user turned off all character options
        if not (use_letters or use_numbers or use_symbols):
            raise ValueError("You must select at least one character type (letters, numbers, or symbols).")

    except ValueError as error_message:
        # This catches bad integer inputs or our custom raised errors
        print(f"\n[Error] Invalid input: {error_message}")
        print("Something went wrong. Please try again.")
        return

    # 2. Build the character pool based on user choices
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    if use_numbers:
        character_pool += string.digits         # 0123456789
    if use_symbols:
        character_pool += string.punctuation    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # 3. Generate the random password
    password = "".join(random.choice(character_pool) for _ in range(length))
    
    print("\n------------------------------")
    print(f"Your Generated Password: {password}")
    print("------------------------------")

# Run the function
generate_password()
