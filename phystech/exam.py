def xor_encrypt_decrypt(input_string, key):
    """Функция для шифрования и расшифровки с использованием XOR."""
    # Преобразуем ключ в список байтов
    key_bytes = key.encode()
    key_length = len(key_bytes)
    print(key_bytes)

    # Шифруем/расшифровываем входную строку
    output = bytearray()
    for i in range(len(input_string)):
        data = input_string[i] ^ key_bytes[i % key_length]
        print(f'i={i}; key_len={key_length}; key_idx={i % key_length}; input_string[i]={input_string[i]}; key_bytes[i % key_length]={key_bytes[i % key_length]}; answer={data}')


        output.append(data)

    return output


def left_rotate(value, shift):
    """Левый сдвиг битов."""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def key_schedule(key):
    """Генерация раундовых ключей из основного ключа."""
    k = [0] * 8
    for i in range(8):
        k[i] = int.from_bytes(key[i*4:(i+1)*4], 'little')
    return k

def encrypt_block(block, k):
    """Шифрование одного блока с использованием ключей."""
    # Начальные значения
    L = block[0]
    R = block[1]

    for i in range(32):
        # Функция F
        temp = (R + k[i % 8]) & 0xFFFFFFFF
        temp = left_rotate(temp, 11)
        temp ^= L

        # Обновление L и R
        L, R = R, temp

    return (R, L)  # Обратите внимание на порядок

def gost_encrypt(data, key):
    """Шифрование данных с использованием ГОСТ 34.12-2018."""
    # Разделение данных на блоки по 8 байт (64 бита)
    blocks = [data[i:i+8] for i in range(0, len(data), 8)]
    k = key_schedule(key)

    encrypted_blocks = []
    for block in blocks:
        # Преобразование блока в два 32-битных целых числа
        L = int.from_bytes(block[:4], 'little')
        R = int.from_bytes(block[4:], 'little')
        encrypted_block = encrypt_block((L, R), k)
        encrypted_blocks.append(encrypted_block[0].to_bytes(4, 'little') + encrypted_block[1].to_bytes(4, 'little'))

    return b''.join(encrypted_blocks)

# Пример использования
if __name__ == "__main__":
    key = b'\x00' * 32  # 256-битный ключ (32 байта)
    message = b'Hello, World!'  # Сообщение для шифрования

    # Дополнение сообщения до кратности 8 байт
    while len(message) % 8 != 0:
        message += b'\x00'

    encrypted_message = gost_encrypt(message, key)
    print("Encrypted message:", encrypted_message)

# # Пример использования
# if __name__ == "__main__":
#     message = "Hello, World!"
#     key = "mysecretkey"
#
#     print("Original message:", message)
#
#     # Шифрование
#     encrypted_message = xor_encrypt_decrypt(message.encode(), key)
#     print("Encrypted message:", encrypted_message)
#
#     # Расшифровка
#     decrypted_message = xor_encrypt_decrypt(encrypted_message, key).decode()
#     print("Decrypted message:", decrypted_message)