import string 

def encrypt(text, shift):
    result = []
    for char in text:
        if char in string.ascii_letters:
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            result.append(chr((ord(char) - base + shift_amount) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

palin_text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))
encrypted_text = encrypt(palin_text, shift)
print(f"Encrypted text: {encrypted_text}")
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")