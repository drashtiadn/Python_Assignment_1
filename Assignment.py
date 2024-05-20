# Encryption 
def encrypt(message, key): 
    encrypted_message = ""  # Initalize empty string to store the encrypted message
    for letter in message: # Loop through each letter
        shifted = ord(letter) + key # Convert the character and add the key
        if shifted > 126: # If shifted value goes beyond printable range, turn it around
            shifted = 32 + (shifted - 127)
        encrypted_message += chr(shifted) # Convert the message back to character and add it to encrypted message
    return encrypted_message # Return final message

# Decryption
def decrypt(encrypted_message, key):
    decrypted_message = ""  # Initalize empty string to store the decrypted message
    for letter in encrypted_message: # Loop through each letter in the encrypted message
        shifted = ord(letter) - key  # Convert the character and subtract the key
        if shifted < 32:  # If shifted value goes beyond printable range, turn it around
            shifted = 127 - (32 - shifted)        
        decrypted_message += chr(shifted) # Convert the message back to character and add it to decrypted message
    return decrypted_message # Return final message

def main():
    message = input("Enter the message: ")  # Get input message from user
    key = int(input("Enter the key (an integer): "))  # Get input integer from user
    mode = input("Choose mode (encrypt/decrypt): ")  # Select mode encrypt or decrypt from user

    if mode == "encrypt": # Check if mode is equal to encrypt
        final = encrypt(message, key) # Call encrypt function and store the value
        print("Encrypted message: ", final) # Print encrypt message
    elif mode == "decrypt": # Check if mode is equal to decrypt
        final = decrypt(message, key) # call decrypt function and store the value
        print("Decrypted message: ", final) # Print decrypt message
    else: # If mode is not equal to encrypt or decrypt
        print("Invalid Mode") # Print an error message

if __name__ == "__main__":   # Check if script is being run directly
    main() # Call main function to excute the program