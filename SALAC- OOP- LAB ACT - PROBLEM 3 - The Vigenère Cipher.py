# PROBLEM 3 - The Vigenère Cipher   SALAC, NICOLETTE IRISH A. BSCpE 1-5

def encrypt_vigenere(plaintext, keyword):
    ciphertext = ''
    keyword_len = len(keyword)
    for i, character in enumerate(plaintext):
        # convert the character to a number
        character_num = ord(character) - ord('A')
        # get the key character for this position
        key_character = keyword[i % keyword_len]
        # convert the key character to a number
        key_num = ord(key_character) - ord('A')
        # add the character and the key together (mod 26 to wrap around)
        cipher_num = (character_num + key_num) % 26
        # convert the cipher number back to a letter and add it to the ciphertext
        ciphertext += chr(cipher_num + ord('A'))
    return ciphertext

#  get users input
plaintext = input("Enter the Plain Text (ALL UPPERCASE LETTERS, NO SPACES): ")
keyword = input("Enter the keyword (ALL UPPERCASE LETTERS): ")

# encrypt the message using the Vigenère cipher
ciphertext = encrypt_vigenere(plaintext, keyword)

# print the ciphertext
print("The ciphertext is:", ciphertext)
