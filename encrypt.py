from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

def encrypt_password(password: str, key: bytes) -> str:
    # Gera um IV (vetor de inicialização) aleatório
    iv = os.urandom(16)

    # Preenche a senha para múltiplos
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(password.encode()) + padder.finalize()

    # Cria o objeto de cifra AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Retorna IV + ciphertext codificados em Base64
    return base64.b64encode(iv + ciphertext).decode()

def decrypt_password(encoded_data: str, key: bytes) -> str:
    data = base64.b64decode(encoded_data)
    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove o preenchimento (unpadding)
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

# Exemplo de uso
if __name__ == "__main__":
    # A chave deve ter exatamente 16, 24 ou 32 bytes
    key = b"chave-secreta123"

    senha = input("Digite a senha para criptografar: ")
    senha_criptografada = encrypt_password(senha, key)
    print(f"🔐 Senha criptografada: {senha_criptografada}")

    senha_descriptografada = decrypt_password(senha_criptografada, key)
    print(f"🔓 Senha original: {senha_descriptografada}")