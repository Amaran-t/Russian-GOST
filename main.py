from pygost import gost28147

def gost_encrypt(message, key):
    cipher = gost28147.GOST28147(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted.hex()

def gost_decrypt(encrypted_message, key):
    cipher = gost28147.GOST28147(key)
    decrypted = cipher.decrypt(bytes.fromhex(encrypted_message))
    return decrypted.decode()

def main():
    choice = input("Введите 'Ш' для шифрования или 'Р' для расшифровки: ").upper()

    if choice == 'Ш':
        message = input("Введите сообщение для шифрования: ")
        key = input("Введите ключ (32 символа): ")

        if len(key) != 32 or not all(c in "0123456789ABCDEFabcdef" for c in key):
            print("Неверная длина ключа или формат. Ключ должен состоять из 32 символов.")
            return

        encrypted_message = gost_encrypt(message, bytes.fromhex(key))
        print("Зашифрованное сообщение:", encrypted_message)

    elif choice == 'Р':
        encrypted_message = input("Введите зашифрованное сообщение: ")
        key = input("Введите ключ (32 шестнадцатеричных символа): ")

        if len(key) != 32 or not all(c in "0123456789ABCDEFabcdef" for c in key):
            print("Неверная длина ключа или формат. Ключ должен состоять из 32 символов.")
            return

        decrypted_message = gost_decrypt(encrypted_message, bytes.fromhex(key))
        print("Расшифрованное сообщение:", decrypted_message)

    else:
        print("Неверный выбор. Введите 'Ш' для шифрования или 'Р' для расшифровки.")

if __name__ == "__main__":
    main()
