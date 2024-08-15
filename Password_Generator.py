# Importing the required modules
import random
import string 

def generate_password(length):
    """ 
    generate a random password of the prescribed length.
     
    Args:
        length (int): The length of the password
        
    Returns:
        str: The generated password.
    """
    # concatenating the constants
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating the Password
    password = ''.join(random.choice(characters) for _ in range (length))

    return password

def main():
    # Asking the user to tell the length of a password
    length = int(input("Enter the length of the password:"))

    # Generating the password
    password = generate_password(length)

    # Printing the password
    print("Generated password: ", password)

if __name__ == "__main__":
    main()   