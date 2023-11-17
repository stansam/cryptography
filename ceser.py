def decrypt_caesar_cipher(encrypted_text):
    decrypted_texts = []

    for shift in range(26):
        decrypted_text = ''
        for char in encrypted_text:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - shift - ord('a')) % 26 + ord('a'))
                decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
            else:
                decrypted_text += char

        decrypted_texts.append(decrypted_text)

    return decrypted_texts

# Example usage:
encrypted_text = "Dwwdfn dw gdzq"
decrypted_texts = decrypt_caesar_cipher(encrypted_text)

print("Possible Decryptions:")
for i, decrypted_text in enumerate(decrypted_texts):
    print(f"Option {i + 1}: {decrypted_text}")
    
