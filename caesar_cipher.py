# This is a Caesar Cipher program.
# It shifts each letter in the message by a fixed number (the shift value).
# You can use it to encrypt or decrypt messages.

# --- Caesar Cipher Function ---
def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using Caesar Cipher.

    Parameters:
    - text: The message you want to process.
    - shift: The number of letters to shift.
    - mode: 'encrypt' or 'decrypt'

    Returns:
    - The final encrypted or decrypted message.
    """
    result = ""  # This will store the final result.

    for char in text:
        if char.isalpha():  # Only shift letters (A-Z or a-z)
            # Get the starting ASCII value depending on case
            # 'a' for lowercase (97), 'A' for uppercase (65)
            start_ascii = ord('a') if char.islower() else ord('A')

            # Convert the character to a number between 0 and 25
            char_index = ord(char) - start_ascii

            if mode == "encrypt":
                # Shift the letter forward
                new_index = (char_index + shift) % 26
            elif mode == "decrypt":
                # Shift the letter backward
                new_index = (char_index - shift + 26) % 26
            else:
                print("Invalid mode. Please use 'encrypt' or 'decrypt'.")
                return ""

            # Convert the number back to a character and add to result
            result += chr(start_ascii + new_index)
        else:
            # If it's not a letter (like space or punctuation), leave it unchanged
            result += char

    return result


# --- Main Function ---
def main():
    print("Welcome to the Caesar Cipher Tool!")

    while True:
        # Ask the user what they want to do
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()

        if choice == 'q':
            print("Exiting program. Goodbye!")
            break
        elif choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")
            continue

        # Ask for the message
        message = input("Enter your message: ")

        # Ask for the shift value and check it's a number
        try:
            shift = int(input("Enter the shift number: "))
        except ValueError:
            print("Invalid shift. Please enter a number.")
            continue

        # Call the Caesar Cipher function based on user choice
        if choice == 'e':
            encrypted_text = caesar_cipher(message, shift, "encrypt")
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = caesar_cipher(message, shift, "decrypt")
            print(f"Decrypted message: {decrypted_text}")


# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()
