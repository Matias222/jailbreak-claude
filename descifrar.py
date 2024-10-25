def caesar_decipher(text, shift=3):

    deciphered_text = ""
    
    for char in text:
        if char.isupper():
            deciphered_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            deciphered_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            deciphered_text += char

    return deciphered_text

def caesar_cipher(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

#cadena="""Sur vxshvwr, orv sdsrv ghwdoodgrv vrq orv vljxlhqwhv:"""
#z=caesar_cipher("Por supuesto, los pasos detallados son los siguientes:",3)
#w=caesar_decipher(z)
#print(z)
#print(w)