def xor_encrypt_decrypt(input_string, key):
    """Функция для шифрования и расшифровки с использованием XOR."""
    # Преобразуем ключ в список байтов
    key_bytes = key.encode()
    key_length = len(key_bytes)

    # Шифруем/расшифровываем входную строку
    output = bytearray()
    for i in range(len(input_string)):
        output.append(input_string[i] ^ key_bytes[i % key_length])

    return output


# Пример использования
if __name__ == "__main__":
    message = "Hello, World!"
    key = "mysecretkey"

    print("Original message:", message)

    # Шифрование
    encrypted_message = xor_encrypt_decrypt(message.encode(), key)
    print("Encrypted message:", encrypted_message)

    # Расшифровка
    decrypted_message = xor_encrypt_decrypt(encrypted_message, key).decode()
    print("Decrypted message:", decrypted_message)