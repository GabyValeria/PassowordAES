from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

def decrypt_password(encoded_data: str, key: bytes) -> str:
    # Decodifica os dados de Base64
    data = base64.b64decode(encoded_data)

    # Extrai IV (primeiros 16 bytes) e o conteúdo criptografado
    iv = data[:16]
    ciphertext = data[16:]

    # Configura a cifra AES com o IV e a chave
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove o padding da mensagem
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

if __name__ == "__main__":
    key = b"chave-secreta123" 
    encoded_input = input("Digite a senha criptografada (Base64): ")
    try:
        senha = decrypt_password(encoded_input, key)
        print(f"🔓 Senha descriptografada: {senha}")
    except Exception as e:
        print("Erro ao descriptografar:", e)